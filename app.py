import copy
import json
import os
import random
import uuid
import ollama

from flask import Flask, render_template, request, jsonify
from database import grade_query, get_correct_output
from generator import generate_problem
from problems import (
    EMPLOYEES, DEPARTMENTS, CUSTOMERS, ORDERS,
    PRODUCTS, PRODUCTS_EXTENDED, ORDER_ITEMS, MONTHLY_REVENUE, STAFF,
    PROBLEMS as _STATIC_PROBLEMS,
)

app = Flask(__name__)
# Prevent Werkzeug from intercepting exceptions and rendering HTML error pages
app.config["PROPAGATE_EXCEPTIONS"] = False

# In-memory problem cache: uuid str -> problem dict
_cache: dict = {}

_TABLE_MAP = {
    "employees":         EMPLOYEES,
    "departments":       DEPARTMENTS,
    "customers":         CUSTOMERS,
    "orders":            ORDERS,
    "products":          PRODUCTS,
    "products_extended": PRODUCTS_EXTENDED,
    "order_items":       ORDER_ITEMS,
    "monthly_revenue":   MONTHLY_REVENUE,
    "staff":             STAFF,
}

_BANK: list | None = None

# All JSON question-bank files in the project directory
_BANK_FILES = [
    "question_bank.json",
    "qb_medium1.json",
    "qb_medium2.json",
    "qb_hard.json",
]


def _get_bank() -> list:
    global _BANK
    if _BANK is not None:
        return _BANK

    bank = list(_STATIC_PROBLEMS)

    base_dir = os.path.dirname(__file__)
    for fname in _BANK_FILES:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, encoding="utf-8") as f:
            extras = json.load(f)
        for q in extras:
            q = q.copy()
            q["tables"] = [_TABLE_MAP[t] for t in q.get("table_names", []) if t in _TABLE_MAP]
            if not q["tables"]:
                continue  # skip entries whose tables aren't in the map
            bank.append(q)

    _BANK = bank
    return _BANK


def _safe_problem(problem: dict) -> dict:
    """Return only browser-safe fields (omits correct_query, etc.)."""
    correct_out = get_correct_output(problem)
    return {
        "id":               problem["id"],
        "title":            problem["title"],
        "difficulty":       problem["difficulty"],
        "category":         problem["category"],
        "description":      problem["description"],
        "question":         problem["question"],
        "hint":             problem.get("hint", ""),
        "tables":           problem["tables"],
        "choices":          [{"id": c["id"], "text": c["text"]} for c in problem["choices"]],
        "expected_columns": correct_out.get("columns", []),
        "expected_rows":    correct_out.get("data", []),
        "expected_error":   correct_out.get("error"),
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(Exception)
def _handle_all(e):
    resp = jsonify({"error": str(e) or type(e).__name__})
    resp.status_code = 500
    return resp


@app.route("/api/bank_list")
def get_bank_list():
    bank = _get_bank()
    items = [
        {
            "index":      i,
            "title":      p["title"],
            "difficulty": p["difficulty"],
            "category":   p["category"],
        }
        for i, p in enumerate(bank)
    ]
    return jsonify(items)


@app.route("/api/bank_problem")
def get_bank_problem():
    bank = _get_bank()

    index_str = request.args.get("index")
    if index_str is not None:
        try:
            idx = int(index_str)
        except ValueError:
            return jsonify({"error": "Invalid index"}), 400
        if idx < 0 or idx >= len(bank):
            return jsonify({"error": "Index out of range"}), 400
        problem = copy.deepcopy(bank[idx])
    else:
        difficulty = request.args.get("difficulty", "All")
        if difficulty in ("Easy", "Medium", "Hard"):
            candidates = [p for p in bank if p["difficulty"] == difficulty] or bank
        else:
            candidates = bank
        topics_raw = request.args.get("topics", "")
        if topics_raw:
            topics_set = {t.strip() for t in topics_raw.split(",") if t.strip()}
            filtered = [p for p in candidates if p.get("category") in topics_set]
            if filtered:
                candidates = filtered
        problem = copy.deepcopy(random.choice(candidates))

    problem["id"] = str(uuid.uuid4())
    _cache[problem["id"]] = problem
    try:
        return jsonify(_safe_problem(problem))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/test_ollama")
def test_ollama():
    """Diagnostic endpoint — visit /api/test_ollama in your browser to check connectivity."""
    results = {}
    try:
        models_resp = ollama.list()
        results["ollama_reachable"] = True
        results["models"] = [m.model for m in (models_resp.models or [])]
    except Exception as e:
        results["ollama_reachable"] = False
        results["reach_error"] = str(e)
        return jsonify(results), 500

    target = "qwen2.5-coder:7b"
    results["target_model"] = target
    results["model_pulled"] = any(target in (m or "") for m in results["models"])

    try:
        resp = ollama.chat(
            model=target,
            messages=[{"role": "user", "content": 'Reply with exactly: {"ok": true}'}],
            format="json",
            options={"temperature": 0},
        )
        results["chat_ok"] = True
        results["chat_reply"] = resp.message.content[:200]
    except Exception as e:
        results["chat_ok"] = False
        results["chat_error"] = str(e)

    return jsonify(results)


@app.route("/api/problem")
def get_problem():
    difficulty = request.args.get("difficulty", "Medium")
    if difficulty not in ("Easy", "Medium", "Hard"):
        difficulty = random.choice(["Easy", "Medium", "Hard"])
    topics_raw = request.args.get("topics", "")
    topics = [t.strip() for t in topics_raw.split(",") if t.strip()] or None
    try:
        problem = generate_problem(difficulty, topics=topics)
        _cache[problem["id"]] = problem
        return jsonify(_safe_problem(problem))
    except Exception as e:
        import traceback
        traceback.print_exc()          # prints full stack to Flask terminal
        return jsonify({"error": str(e)}), 500


@app.route("/api/submit", methods=["POST"])
def submit():
    data       = request.json or {}
    pid        = data.get("problem_id")
    user_query = (data.get("query") or "").strip()
    chosen_id  = data.get("choice")

    problem = _cache.get(pid)
    if not problem:
        return jsonify({"error": "Problem not found — please load a new question."}), 404

    result = {
        "explanation":    problem["explanation"],
        "choices_graded": problem["choices"],
    }

    if user_query:
        result["query_graded"] = grade_query(problem, user_query)

    if chosen_id:
        chosen = next((c for c in problem["choices"] if c["id"] == chosen_id), None)
        if chosen:
            result["choice_correct"]  = chosen["correct"]
            result["choice_selected"] = chosen_id

    return jsonify(result)


if __name__ == "__main__":
    print(f"[app.py] Loading from: {os.path.abspath(__file__)}")
    print("[app.py] Routes registered:", [r.rule for r in app.url_map.iter_rules()])
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, port=5000, use_reloader=False)
