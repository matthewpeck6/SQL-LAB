import duckdb
import decimal


def _serialize(v):
    if v is None:
        return None
    if isinstance(v, decimal.Decimal):
        return float(v)
    if hasattr(v, "isoformat"):
        return v.isoformat()
    return v


def _normalize(v):
    if v is None:
        return "NULL"
    if isinstance(v, decimal.Decimal):
        v = float(v)
    if isinstance(v, float) and float(v) == int(float(v)):
        return str(int(float(v)))
    if isinstance(v, float):
        return str(round(v, 4))
    if hasattr(v, "isoformat"):
        return v.isoformat()
    return str(v)


def setup_db(problem):
    conn = duckdb.connect(":memory:")
    for table in problem["tables"]:
        col_defs = ", ".join(
            f'"{c["name"]}" {c["type"]}' for c in table["columns"]
        )
        conn.execute(f'CREATE TABLE "{table["name"]}" ({col_defs})')
        col_names = [c["name"] for c in table["columns"]]
        for row in table.get("data", []):
            vals = [row.get(c) for c in col_names]
            placeholders = ", ".join("?" for _ in vals)
            cols_str = ", ".join(f'"{c}"' for c in col_names)
            conn.execute(
                f'INSERT INTO "{table["name"]}" ({cols_str}) VALUES ({placeholders})',
                vals,
            )
    return conn


def _run(conn, query):
    cur = conn.execute(query)
    columns = [d[0] for d in cur.description]
    rows = cur.fetchall()
    data = [{col: _serialize(val) for col, val in zip(columns, row)} for row in rows]
    return {"data": data, "columns": columns}


def get_correct_output(problem):
    try:
        conn = setup_db(problem)
        result = _run(conn, problem["correct_query"])
        conn.close()
        return result
    except Exception as e:
        return {"error": str(e)}


def grade_query(problem, user_query):
    try:
        conn = setup_db(problem)
        user_result = _run(conn, user_query)
        correct_result = _run(conn, problem["correct_query"])
        conn.close()

        is_correct = _compare(
            user_result["data"],
            correct_result["data"],
            problem.get("order_matters", False),
        )
        return {
            "user_data": user_result["data"],
            "user_columns": user_result["columns"],
            "correct_data": correct_result["data"],
            "correct_columns": correct_result["columns"],
            "is_correct": is_correct,
            "user_row_count": len(user_result["data"]),
            "correct_row_count": len(correct_result["data"]),
        }
    except Exception as e:
        return {"error": str(e)}


def _compare(user, correct, order_matters):
    if len(user) != len(correct):
        return False

    def norm_row(row):
        return tuple(_normalize(v) for v in row.values())

    u = [norm_row(r) for r in user]
    c = [norm_row(r) for r in correct]
    return u == c if order_matters else sorted(u) == sorted(c)
