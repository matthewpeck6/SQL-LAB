import ollama
import json
import uuid

from database import get_correct_output
from problems import (
    EMPLOYEES, DEPARTMENTS, CUSTOMERS, ORDERS,
    PRODUCTS, ORDER_ITEMS, MONTHLY_REVENUE, STAFF,
)

# Change this to any model you have pulled in Ollama.
# Recommended: qwen2.5-coder:7b (best SQL quality at ~4.5 GB)
# Alternatives: llama3.2:latest, deepseek-coder-v2:16b (better but 9 GB)
OLLAMA_MODEL = "qwen2.5-coder:7b"

ALL_TABLES = {
    "employees":       EMPLOYEES,
    "departments":     DEPARTMENTS,
    "customers":       CUSTOMERS,
    "orders":          ORDERS,
    "products":        PRODUCTS,
    "order_items":     ORDER_ITEMS,
    "monthly_revenue": MONTHLY_REVENUE,
    "staff":           STAFF,
}

_DIFFICULTY_GUIDE = {
    "Easy": (
        "Use 1-2 tables. Apply one or two of: simple JOIN, GROUP BY + aggregate "
        "(SUM/COUNT/AVG/MAX/MIN), or a basic window function (ROW_NUMBER/RANK/DENSE_RANK). "
        "No CTEs required. Keep the query under 12 lines."
    ),
    "Medium": (
        "Use 2-3 tables. Combine at least two distinct concepts: "
        "JOIN + window function, subquery + aggregation, or a CTE with aggregation. "
        "Require understanding of multiple SQL features."
    ),
    "Hard": (
        "Use 3+ tables (or a self-join on staff). "
        "Combine CTEs, window functions, subqueries, and complex aggregations together. "
        "The query must be sophisticated and test deep SQL knowledge."
    ),
}

_SYSTEM = (
    "You are an expert SQL instructor. "
    "Generate SQL practice problems using DuckDB-compatible SQL (standard ANSI SQL). "
    "Do NOT use MySQL-specific syntax. "
    "Always respond with a single valid JSON object and nothing else."
)


def _check_ollama():
    """Raise a clear RuntimeError if the Ollama server is not reachable."""
    try:
        ollama.list()
    except Exception:
        raise RuntimeError(
            "Cannot connect to Ollama. "
            "Make sure the Ollama app is running (or run 'ollama serve' in a terminal), "
            f"then ensure the model is pulled: ollama pull {OLLAMA_MODEL}"
        )


def _schema_summary() -> str:
    parts = []
    for name, table in ALL_TABLES.items():
        cols = ", ".join(f"{c['name']} {c['type']}" for c in table["columns"])
        rows = " | ".join(
            ", ".join(f"{k}={v!r}" for k, v in list(r.items())[:4])
            for r in table["data"][:2]
        )
        parts.append(f"  {name}({cols})\n    sample: {rows}")
    return "\n".join(parts)


def _user_prompt(difficulty: str, topics: list | None = None) -> str:
    if topics:
        joined = " and ".join(topics) if len(topics) <= 3 else ", ".join(topics)
        topic_line = f"\nThe problem MUST focus specifically on: {joined}\n"
    else:
        topic_line = ""
    return f"""Create a {difficulty}-difficulty SQL practice problem using these tables:

{_schema_summary()}

Difficulty: {_DIFFICULTY_GUIDE[difficulty]}{topic_line}
Draw from: Subqueries, JOINs (INNER/LEFT/RIGHT), Window Functions (ROW_NUMBER/RANK/DENSE_RANK/LAG/LEAD/SUM OVER/AVG OVER), CTEs (WITH clause), Aggregations (GROUP BY/HAVING/SUM/AVG/COUNT/MAX/MIN).

Return a JSON object with EXACTLY these fields:
{{
  "title": "Short title 5-8 words",
  "category": "e.g. Window Functions or CTEs and Aggregation or Joins and Subqueries",
  "description": "2-3 sentence business context",
  "question": "Precise task: which columns, filters, ordering, limits",
  "hint": "One sentence naming the key SQL constructs",
  "tables": ["table_name1", "table_name2"],
  "correct_query": "SELECT ... complete runnable DuckDB SQL",
  "order_matters": false,
  "explanation": "Step by step explanation using **KEYWORD** for SQL terms",
  "choices": [
    {{"id": "A", "text": "SELECT ...", "correct": true,  "explanation": "CORRECT. Why this works."}},
    {{"id": "B", "text": "SELECT ...", "correct": false, "explanation": "INCORRECT. Specific error."}},
    {{"id": "C", "text": "SELECT ...", "correct": false, "explanation": "INCORRECT. Specific error."}},
    {{"id": "D", "text": "SELECT ...", "correct": false, "explanation": "INCORRECT. Specific error."}}
  ]
}}

Rules:
- correct_query MUST return at least 1 row with the sample data shown above
- All 4 choices must be complete runnable SQL (wrong choices produce wrong results, not errors)
- Wrong choices must have subtle errors: wrong JOIN type, missing PARTITION BY, wrong ORDER, etc.
- tables list must only use: employees, departments, customers, orders, products, order_items, monthly_revenue, staff"""


def generate_problem(difficulty: str = "Medium", topics: list | None = None, max_retries: int = 3) -> dict:
    if difficulty not in _DIFFICULTY_GUIDE:
        difficulty = "Medium"

    _check_ollama()

    last_err = None

    for attempt in range(max_retries + 1):
        try:
            response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": _SYSTEM},
                    {"role": "user",   "content": _user_prompt(difficulty, topics)},
                ],
                format="json",
                options={"temperature": 0.7},
            )
            raw = response.message.content.strip()
            parsed = json.loads(raw)
            problem = _build_problem(parsed, difficulty)
            _validate(problem)
            return problem
        except Exception as e:
            last_err = e

    raise RuntimeError(
        f"Generation failed after {max_retries + 1} attempts. "
        f"Last error: {last_err}. "
        f"Make sure Ollama is running and '{OLLAMA_MODEL}' is pulled "
        f"(run: ollama pull {OLLAMA_MODEL})."
    )


def _build_problem(parsed: dict, difficulty: str) -> dict:
    table_names = parsed.get("tables", [])
    tables = [ALL_TABLES[n] for n in table_names if n in ALL_TABLES]
    if not tables:
        raise ValueError(f"No valid tables found in response: {table_names}")

    choices = parsed.get("choices", [])
    if len(choices) != 4:
        raise ValueError(f"Expected 4 choices, got {len(choices)}")

    return {
        "id":            str(uuid.uuid4()),
        "title":         parsed["title"],
        "difficulty":    difficulty,
        "category":      parsed["category"],
        "description":   parsed["description"],
        "question":      parsed["question"],
        "hint":          parsed.get("hint", ""),
        "tables":        tables,
        "correct_query": parsed["correct_query"],
        "order_matters": bool(parsed.get("order_matters", False)),
        "explanation":   parsed["explanation"],
        "choices":       choices,
    }


def _validate(problem: dict) -> None:
    result = get_correct_output(problem)
    if "error" in result:
        raise ValueError(f"Correct query failed in DuckDB: {result['error']}")
    if not result.get("data"):
        raise ValueError("Correct query returned 0 rows — regenerating")
