# ─────────────────────────────────────────────────────────────
#  Shared dataset definitions
# ─────────────────────────────────────────────────────────────

EMPLOYEES = {
    "name": "employees",
    "columns": [
        {"name": "employee_id", "type": "INTEGER"},
        {"name": "name",        "type": "VARCHAR"},
        {"name": "department_id", "type": "INTEGER"},
        {"name": "salary",      "type": "DECIMAL(10,2)"},
        {"name": "hire_date",   "type": "DATE"},
    ],
    "data": [
        {"employee_id": 1,  "name": "Alice Johnson",   "department_id": 1, "salary": 95000.00, "hire_date": "2020-01-15"},
        {"employee_id": 2,  "name": "Bob Smith",        "department_id": 1, "salary": 85000.00, "hire_date": "2019-03-22"},
        {"employee_id": 3,  "name": "Carol Williams",   "department_id": 1, "salary": 95000.00, "hire_date": "2021-07-01"},
        {"employee_id": 4,  "name": "David Brown",      "department_id": 2, "salary": 110000.00, "hire_date": "2018-11-10"},
        {"employee_id": 5,  "name": "Emma Davis",       "department_id": 2, "salary": 98000.00, "hire_date": "2020-05-20"},
        {"employee_id": 6,  "name": "Frank Miller",     "department_id": 2, "salary": 110000.00, "hire_date": "2017-08-15"},
        {"employee_id": 7,  "name": "Grace Wilson",     "department_id": 3, "salary": 72000.00, "hire_date": "2022-01-10"},
        {"employee_id": 8,  "name": "Henry Moore",      "department_id": 3, "salary": 78000.00, "hire_date": "2021-04-05"},
        {"employee_id": 9,  "name": "Isabel Taylor",    "department_id": 3, "salary": 72000.00, "hire_date": "2022-06-20"},
        {"employee_id": 10, "name": "James Anderson",   "department_id": 1, "salary": 75000.00, "hire_date": "2023-02-01"},
    ],
}

DEPARTMENTS = {
    "name": "departments",
    "columns": [
        {"name": "department_id",   "type": "INTEGER"},
        {"name": "department_name", "type": "VARCHAR"},
        {"name": "location",        "type": "VARCHAR"},
        {"name": "budget",          "type": "DECIMAL(12,2)"},
    ],
    "data": [
        {"department_id": 1, "department_name": "Engineering", "location": "New York",     "budget": 600000.00},
        {"department_id": 2, "department_name": "Sales",       "location": "Chicago",      "budget": 450000.00},
        {"department_id": 3, "department_name": "Marketing",   "location": "Los Angeles",  "budget": 350000.00},
        {"department_id": 4, "department_name": "HR",          "location": "Boston",       "budget": 200000.00},
    ],
}

CUSTOMERS = {
    "name": "customers",
    "columns": [
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "name",        "type": "VARCHAR"},
        {"name": "city",        "type": "VARCHAR"},
        {"name": "country",     "type": "VARCHAR"},
    ],
    "data": [
        {"customer_id": 1,  "name": "Alice Chen",       "city": "New York",    "country": "USA"},
        {"customer_id": 2,  "name": "Bob Martinez",     "city": "Chicago",     "country": "USA"},
        {"customer_id": 3,  "name": "Carol Lee",        "city": "Los Angeles", "country": "USA"},
        {"customer_id": 4,  "name": "David Kim",        "city": "Houston",     "country": "USA"},
        {"customer_id": 5,  "name": "Emma Rodriguez",   "city": "Phoenix",     "country": "USA"},
        {"customer_id": 6,  "name": "Frank Johnson",    "city": "San Antonio", "country": "USA"},
        {"customer_id": 7,  "name": "Grace Brown",      "city": "San Diego",   "country": "USA"},
        {"customer_id": 8,  "name": "Henry Davis",      "city": "Dallas",      "country": "USA"},
        {"customer_id": 9,  "name": "Isabel Wilson",    "city": "San Jose",    "country": "USA"},
        {"customer_id": 10, "name": "James Taylor",     "city": "Austin",      "country": "USA"},
        {"customer_id": 11, "name": "Oliver White",     "city": "Denver",      "country": "USA"},
        {"customer_id": 12, "name": "Sophia Harris",    "city": "Seattle",     "country": "USA"},
    ],
}

ORDERS = {
    "name": "orders",
    "columns": [
        {"name": "order_id",     "type": "INTEGER"},
        {"name": "customer_id",  "type": "INTEGER"},
        {"name": "order_date",   "type": "DATE"},
        {"name": "total_amount", "type": "DECIMAL(10,2)"},
    ],
    "data": [
        {"order_id": 1,  "customer_id": 1,  "order_date": "2024-01-05", "total_amount": 1299.99},
        {"order_id": 2,  "customer_id": 2,  "order_date": "2024-01-10", "total_amount": 109.97},
        {"order_id": 3,  "customer_id": 1,  "order_date": "2024-01-20", "total_amount": 429.98},
        {"order_id": 4,  "customer_id": 3,  "order_date": "2024-02-01", "total_amount": 549.99},
        {"order_id": 5,  "customer_id": 2,  "order_date": "2024-02-15", "total_amount": 399.99},
        {"order_id": 6,  "customer_id": 4,  "order_date": "2024-02-20", "total_amount": 1299.99},
        {"order_id": 7,  "customer_id": 1,  "order_date": "2024-03-05", "total_amount": 239.98},
        {"order_id": 8,  "customer_id": 5,  "order_date": "2024-03-10", "total_amount": 109.98},
        {"order_id": 9,  "customer_id": 3,  "order_date": "2024-03-15", "total_amount": 151.95},
        {"order_id": 10, "customer_id": 6,  "order_date": "2024-03-20", "total_amount": 349.99},
        {"order_id": 11, "customer_id": 7,  "order_date": "2024-04-01", "total_amount": 144.93},
        {"order_id": 12, "customer_id": 2,  "order_date": "2024-04-10", "total_amount": 149.99},
        {"order_id": 13, "customer_id": 8,  "order_date": "2024-04-15", "total_amount": 549.99},
        {"order_id": 14, "customer_id": 1,  "order_date": "2024-04-20", "total_amount": 79.98},
        {"order_id": 15, "customer_id": 9,  "order_date": "2024-05-01", "total_amount": 1299.99},
        {"order_id": 16, "customer_id": 3,  "order_date": "2024-05-10", "total_amount": 79.99},
        {"order_id": 17, "customer_id": 10, "order_date": "2024-05-15", "total_amount": 399.99},
        {"order_id": 18, "customer_id": 4,  "order_date": "2024-05-20", "total_amount": 395.98},
        {"order_id": 19, "customer_id": 5,  "order_date": "2024-06-01", "total_amount": 1299.99},
        {"order_id": 20, "customer_id": 6,  "order_date": "2024-06-10", "total_amount": 299.98},
    ],
}

PRODUCTS = {
    "name": "products",
    "columns": [
        {"name": "product_id", "type": "INTEGER"},
        {"name": "name",       "type": "VARCHAR"},
        {"name": "category",   "type": "VARCHAR"},
        {"name": "price",      "type": "DECIMAL(10,2)"},
    ],
    "data": [
        {"product_id": 1,  "name": "Laptop Pro",         "category": "Electronics", "price": 1299.99},
        {"product_id": 2,  "name": "Wireless Mouse",     "category": "Electronics", "price": 29.99},
        {"product_id": 3,  "name": "USB-C Hub",          "category": "Electronics", "price": 49.99},
        {"product_id": 4,  "name": "Standing Desk",      "category": "Furniture",   "price": 549.99},
        {"product_id": 5,  "name": "Office Chair",       "category": "Furniture",   "price": 399.99},
        {"product_id": 6,  "name": "Monitor 27in",       "category": "Electronics", "price": 349.99},
        {"product_id": 7,  "name": "Mech Keyboard",      "category": "Electronics", "price": 79.99},
        {"product_id": 8,  "name": "Desk Lamp",          "category": "Furniture",   "price": 45.99},
        {"product_id": 9,  "name": "Notebook Set",       "category": "Stationery",  "price": 19.99},
        {"product_id": 10, "name": "Pen Pack",           "category": "Stationery",  "price": 8.99},
        {"product_id": 11, "name": "Webcam HD",          "category": "Electronics", "price": 89.99},
        {"product_id": 12, "name": "Headphones",         "category": "Electronics", "price": 149.99},
    ],
}

ORDER_ITEMS = {
    "name": "order_items",
    "columns": [
        {"name": "item_id",    "type": "INTEGER"},
        {"name": "order_id",   "type": "INTEGER"},
        {"name": "product_id", "type": "INTEGER"},
        {"name": "quantity",   "type": "INTEGER"},
        {"name": "unit_price", "type": "DECIMAL(10,2)"},
    ],
    "data": [
        {"item_id": 1,  "order_id": 1,  "product_id": 1,  "quantity": 1, "unit_price": 1299.99},
        {"item_id": 2,  "order_id": 2,  "product_id": 2,  "quantity": 2, "unit_price": 29.99},
        {"item_id": 3,  "order_id": 2,  "product_id": 3,  "quantity": 1, "unit_price": 49.99},
        {"item_id": 4,  "order_id": 3,  "product_id": 6,  "quantity": 1, "unit_price": 349.99},
        {"item_id": 5,  "order_id": 3,  "product_id": 7,  "quantity": 1, "unit_price": 79.99},
        {"item_id": 6,  "order_id": 4,  "product_id": 4,  "quantity": 1, "unit_price": 549.99},
        {"item_id": 7,  "order_id": 5,  "product_id": 5,  "quantity": 1, "unit_price": 399.99},
        {"item_id": 8,  "order_id": 6,  "product_id": 1,  "quantity": 1, "unit_price": 1299.99},
        {"item_id": 9,  "order_id": 7,  "product_id": 11, "quantity": 1, "unit_price": 89.99},
        {"item_id": 10, "order_id": 7,  "product_id": 12, "quantity": 1, "unit_price": 149.99},
        {"item_id": 11, "order_id": 8,  "product_id": 7,  "quantity": 1, "unit_price": 79.99},
        {"item_id": 12, "order_id": 8,  "product_id": 2,  "quantity": 1, "unit_price": 29.99},
        {"item_id": 13, "order_id": 9,  "product_id": 8,  "quantity": 2, "unit_price": 45.99},
        {"item_id": 14, "order_id": 9,  "product_id": 9,  "quantity": 3, "unit_price": 19.99},
        {"item_id": 15, "order_id": 10, "product_id": 6,  "quantity": 1, "unit_price": 349.99},
        {"item_id": 16, "order_id": 11, "product_id": 3,  "quantity": 2, "unit_price": 49.99},
        {"item_id": 17, "order_id": 11, "product_id": 10, "quantity": 5, "unit_price": 8.99},
        {"item_id": 18, "order_id": 12, "product_id": 12, "quantity": 1, "unit_price": 149.99},
        {"item_id": 19, "order_id": 13, "product_id": 4,  "quantity": 1, "unit_price": 549.99},
        {"item_id": 20, "order_id": 14, "product_id": 3,  "quantity": 1, "unit_price": 49.99},
        {"item_id": 21, "order_id": 14, "product_id": 2,  "quantity": 1, "unit_price": 29.99},
        {"item_id": 22, "order_id": 15, "product_id": 1,  "quantity": 1, "unit_price": 1299.99},
        {"item_id": 23, "order_id": 16, "product_id": 7,  "quantity": 1, "unit_price": 79.99},
        {"item_id": 24, "order_id": 17, "product_id": 5,  "quantity": 1, "unit_price": 399.99},
        {"item_id": 25, "order_id": 18, "product_id": 6,  "quantity": 1, "unit_price": 349.99},
        {"item_id": 26, "order_id": 18, "product_id": 8,  "quantity": 1, "unit_price": 45.99},
        {"item_id": 27, "order_id": 19, "product_id": 1,  "quantity": 1, "unit_price": 1299.99},
        {"item_id": 28, "order_id": 20, "product_id": 12, "quantity": 2, "unit_price": 149.99},
    ],
}

MONTHLY_REVENUE = {
    "name": "monthly_revenue",
    "columns": [
        {"name": "year",    "type": "INTEGER"},
        {"name": "month",   "type": "INTEGER"},
        {"name": "revenue", "type": "DECIMAL(12,2)"},
    ],
    "data": [
        {"year": 2023, "month": 1,  "revenue": 125000},
        {"year": 2023, "month": 2,  "revenue": 138000},
        {"year": 2023, "month": 3,  "revenue": 142000},
        {"year": 2023, "month": 4,  "revenue": 135000},
        {"year": 2023, "month": 5,  "revenue": 158000},
        {"year": 2023, "month": 6,  "revenue": 162000},
        {"year": 2023, "month": 7,  "revenue": 155000},
        {"year": 2023, "month": 8,  "revenue": 148000},
        {"year": 2023, "month": 9,  "revenue": 172000},
        {"year": 2023, "month": 10, "revenue": 185000},
        {"year": 2023, "month": 11, "revenue": 198000},
        {"year": 2023, "month": 12, "revenue": 220000},
        {"year": 2024, "month": 1,  "revenue": 195000},
        {"year": 2024, "month": 2,  "revenue": 182000},
        {"year": 2024, "month": 3,  "revenue": 210000},
        {"year": 2024, "month": 4,  "revenue": 225000},
        {"year": 2024, "month": 5,  "revenue": 240000},
        {"year": 2024, "month": 6,  "revenue": 258000},
    ],
}

STAFF = {
    "name": "staff",
    "columns": [
        {"name": "staff_id",   "type": "INTEGER"},
        {"name": "name",       "type": "VARCHAR"},
        {"name": "manager_id", "type": "INTEGER"},
        {"name": "department", "type": "VARCHAR"},
        {"name": "salary",     "type": "DECIMAL(10,2)"},
        {"name": "hire_date",  "type": "DATE"},
    ],
    "data": [
        {"staff_id": 1,  "name": "Sarah Connor",  "manager_id": None, "department": "Executive",   "salary": 250000, "hire_date": "2015-01-01"},
        {"staff_id": 2,  "name": "John Smith",    "manager_id": 1,    "department": "Engineering", "salary": 120000, "hire_date": "2016-03-15"},
        {"staff_id": 3,  "name": "Mary Jones",    "manager_id": 1,    "department": "Sales",       "salary": 115000, "hire_date": "2016-06-20"},
        {"staff_id": 4,  "name": "Tom Baker",     "manager_id": 2,    "department": "Engineering", "salary": 95000,  "hire_date": "2018-09-10"},
        {"staff_id": 5,  "name": "Lisa White",    "manager_id": 2,    "department": "Engineering", "salary": 88000,  "hire_date": "2019-02-14"},
        {"staff_id": 6,  "name": "Jack Brown",    "manager_id": 3,    "department": "Sales",       "salary": 82000,  "hire_date": "2019-07-01"},
        {"staff_id": 7,  "name": "Amy Davis",     "manager_id": 3,    "department": "Sales",       "salary": 78000,  "hire_date": "2020-01-20"},
        {"staff_id": 8,  "name": "Mike Wilson",   "manager_id": 2,    "department": "Engineering", "salary": 92000,  "hire_date": "2019-11-05"},
        {"staff_id": 9,  "name": "Kate Moore",    "manager_id": 3,    "department": "Sales",       "salary": 85000,  "hire_date": "2020-08-15"},
        {"staff_id": 10, "name": "Bob Taylor",    "manager_id": 2,    "department": "Engineering", "salary": 75000,  "hire_date": "2021-03-22"},
    ],
}

# PRODUCTS variant that includes two never-ordered items (for NULL-handling problems)
PRODUCTS_EXTENDED = {
    "name": "products",
    "columns": PRODUCTS["columns"],
    "data": PRODUCTS["data"] + [
        {"product_id": 13, "name": "Whiteboard",    "category": "Furniture",  "price": 89.99},
        {"product_id": 14, "name": "Ergonomic Mat", "category": "Stationery", "price": 34.99},
    ],
}

# ─────────────────────────────────────────────────────────────
#  Problem definitions
# ─────────────────────────────────────────────────────────────

PROBLEMS = [

    # ── 1 ────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "Employee Salary Rankings Within Departments",
        "difficulty": "Medium",
        "category": "Window Functions",
        "description": (
            "The HR department wants to compare salaries within each team. "
            "You need to rank every employee by salary inside their department "
            "so managers can quickly spot where each person stands relative to peers."
        ),
        "question": (
            "Write a query that returns each employee's name, department name, salary, "
            "and their salary rank within the department (highest = 1). "
            "Use DENSE_RANK() so tied salaries share the same rank number. "
            "Order results by department name, then rank."
        ),
        "hint": "Use DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC). Join employees to departments to get the name.",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
SELECT
    e.name,
    d.department_name,
    e.salary,
    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, salary_rank, e.name;""",
        "order_matters": False,
        "explanation": (
            "**JOIN** is required to bring department_name from the departments table.\n\n"
            "**DENSE_RANK() OVER (PARTITION BY ... ORDER BY ...)**:\n"
            "- PARTITION BY department_id restarts the ranking for each department.\n"
            "- ORDER BY salary DESC means the highest earner gets rank 1.\n"
            "- DENSE_RANK() never skips a rank number when there are ties "
            "(contrast: RANK() would skip — two rank-1 ties → next is rank 3).\n\n"
            "If you used RANK() instead of DENSE_RANK(), tied salaries would still both "
            "get rank 1, but the next distinct salary would jump to rank 3 (gap exists)."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    DENSE_RANK() OVER (PARTITION BY e.department_id
                       ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, salary_rank;""",
                "correct": True,
                "explanation": "CORRECT. DENSE_RANK() with PARTITION BY department_id ranks within each department; ORDER BY salary DESC puts the highest earner at rank 1. The JOIN supplies department_name.",
            },
            {
                "id": "B",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    RANK() OVER (ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, salary_rank;""",
                "correct": False,
                "explanation": "INCORRECT. Missing PARTITION BY — this produces a single global ranking across all employees rather than a per-department ranking. Also uses RANK() not DENSE_RANK().",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    DENSE_RANK() OVER (PARTITION BY e.department_id
                       ORDER BY e.salary ASC) AS salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, salary_rank;""",
                "correct": False,
                "explanation": "INCORRECT. ORDER BY salary ASC assigns rank 1 to the lowest-paid employee, which is the opposite of what is asked (highest = rank 1).",
            },
            {
                "id": "D",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    DENSE_RANK() OVER (PARTITION BY d.department_name
                       ORDER BY e.salary DESC) AS salary_rank
FROM employees e
CROSS JOIN departments d
ORDER BY d.department_name, salary_rank;""",
                "correct": False,
                "explanation": "INCORRECT. CROSS JOIN creates every combination of employees × departments (40 rows instead of 10). A regular JOIN on department_id is needed.",
            },
        ],
    },

    # ── 2 ────────────────────────────────────────────────────
    {
        "id": 2,
        "title": "Top 3 Customers by Total Spending",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "The sales team wants to identify the three highest-spending customers "
            "to invite them to an exclusive loyalty program. "
            "You have a customers table and an orders table linked by customer_id."
        ),
        "question": (
            "Write a query that returns the top 3 customers ranked by their total spending. "
            "Include customer name, total number of orders, and total amount spent (rounded to 2 decimals). "
            "Name the aggregated columns order_count and total_spent."
        ),
        "hint": "JOIN customers to orders, GROUP BY customer, SUM(total_amount), then ORDER BY total_spent DESC LIMIT 3.",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
SELECT
    c.name AS customer_name,
    COUNT(o.order_id)          AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 3;""",
        "order_matters": True,
        "explanation": (
            "**JOIN** links each order to its customer.\n\n"
            "**GROUP BY c.customer_id, c.name** collapses all orders per customer into one row. "
            "Including customer_id in GROUP BY is best practice — it avoids ambiguity if two "
            "customers share a name.\n\n"
            "**SUM(o.total_amount)** adds up all order values for that customer. "
            "**COUNT(o.order_id)** counts distinct orders.\n\n"
            "**ORDER BY total_spent DESC LIMIT 3** keeps only the top 3 rows.\n\n"
            "Customers 11 (Oliver White) and 12 (Sophia Harris) have no orders, so they are "
            "excluded automatically by the INNER JOIN — no WHERE clause needed."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT c.name AS customer_name,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 3;""",
                "correct": True,
                "explanation": "CORRECT. Joins, groups by customer, aggregates order count and total spend, then takes the top 3 by descending spend.",
            },
            {
                "id": "B",
                "text": """\
SELECT c.name AS customer_name,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 3;""",
                "correct": False,
                "explanation": "INCORRECT. LEFT JOIN includes customers with no orders (NULL total_spent = 0 after ROUND). This could displace a real top spender if the dataset had very few orders — and it returns the same 3 here only by coincidence. For 'top spenders' an INNER JOIN is semantically correct.",
            },
            {
                "id": "C",
                "text": """\
SELECT c.name AS customer_name,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 3;""",
                "correct": False,
                "explanation": "INCORRECT. GROUP BY c.name only — if two customers shared the same name their data would be merged into a single row, producing wrong totals.",
            },
            {
                "id": "D",
                "text": """\
SELECT c.name AS customer_name,
    COUNT(*) AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c, orders o
WHERE c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent
LIMIT 3;""",
                "correct": False,
                "explanation": "INCORRECT. ORDER BY total_spent (ascending) returns the three lowest spenders, not the top 3. DESC is required.",
            },
        ],
    },

    # ── 3 ────────────────────────────────────────────────────
    {
        "id": 3,
        "title": "Employees Earning Above Their Department Average",
        "difficulty": "Hard",
        "category": "Subqueries",
        "description": (
            "Finance needs a list of employees whose salary is above the average for their "
            "specific department — not the company-wide average. "
            "This requires comparing each row to a group-level statistic."
        ),
        "question": (
            "Write a query returning each above-average earner's name, department name, "
            "salary, and the department's average salary (rounded to 2 decimals, aliased dept_avg). "
            "Use a correlated subquery or a derived table — not a CTE."
        ),
        "hint": "Correlated subquery: WHERE e.salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department_id = e.department_id)",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
SELECT
    e.name,
    d.department_name,
    e.salary,
    ROUND((SELECT AVG(salary) FROM employees e2
           WHERE e2.department_id = e.department_id), 2) AS dept_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
)
ORDER BY d.department_name, e.salary DESC;""",
        "order_matters": False,
        "explanation": (
            "A **correlated subquery** runs once per outer row. "
            "The inner query references e.department_id from the outer query, "
            "which changes as the database steps through each employee.\n\n"
            "Department averages:\n"
            "- Engineering: (95k+85k+95k+75k)/4 = 87,500 → Alice (95k) and Carol (95k) qualify\n"
            "- Sales: (110k+98k+110k)/3 = 106,000 → David (110k) and Frank (110k) qualify\n"
            "- Marketing: (72k+78k+72k)/3 = 74,000 → Henry (78k) qualifies\n\n"
            "The same logic works with a derived table in the FROM clause:\n"
            "JOIN (SELECT department_id, AVG(salary) AS dept_avg FROM employees GROUP BY department_id) avg_t\n"
            "ON e.department_id = avg_t.department_id WHERE e.salary > avg_t.dept_avg"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    ROUND((SELECT AVG(salary) FROM employees e2
           WHERE e2.department_id = e.department_id), 2) AS dept_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(salary) FROM employees e2
    WHERE e2.department_id = e.department_id
)
ORDER BY d.department_name, e.salary DESC;""",
                "correct": True,
                "explanation": "CORRECT. A correlated subquery in the WHERE clause filters to above-average earners. A second correlated subquery in SELECT shows the actual department average.",
            },
            {
                "id": "B",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    ROUND(AVG(e.salary) OVER (PARTITION BY e.department_id), 2) AS dept_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > AVG(e.salary) OVER (PARTITION BY e.department_id)
ORDER BY d.department_name, e.salary DESC;""",
                "correct": False,
                "explanation": "INCORRECT. You cannot use a window function directly inside a WHERE clause — window functions are evaluated after WHERE filtering. You would need to wrap this in a subquery or CTE first.",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    ROUND(AVG(e.salary), 2) AS dept_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > AVG(e.salary)
GROUP BY e.employee_id, e.name, d.department_name, e.salary
ORDER BY d.department_name, e.salary DESC;""",
                "correct": False,
                "explanation": "INCORRECT. AVG() in a WHERE clause is illegal — aggregate functions cannot filter rows directly. Use HAVING for aggregated conditions, but even then this logic doesn't compare to the department average.",
            },
            {
                "id": "D",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    ROUND(avg_t.dept_avg, 2) AS dept_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN (SELECT department_id, AVG(salary) AS dept_avg
      FROM employees GROUP BY department_id) avg_t
  ON e.department_id = avg_t.department_id
WHERE e.salary > avg_t.dept_avg
ORDER BY d.department_name, e.salary DESC;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Uses a derived table instead of a correlated subquery — joining the pre-aggregated averages then filtering. Both approaches produce identical results.",
            },
        ],
    },

    # ── 4 ────────────────────────────────────────────────────
    {
        "id": 4,
        "title": "Top Earner Per Department Using a CTE",
        "difficulty": "Hard",
        "category": "CTEs (Common Table Expressions)",
        "description": (
            "HR wants exactly one employee per department — the highest-paid person. "
            "When salaries tie, pick the employee who was hired first. "
            "Use a CTE to keep the query readable."
        ),
        "question": (
            "Write a query using a CTE that returns the name, department name, salary, "
            "and hire date of the top-earning employee in each department. "
            "Break salary ties by choosing the earlier hire date."
        ),
        "hint": "WITH ranked AS (SELECT ..., ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC, hire_date ASC) AS rn ...) SELECT ... FROM ranked WHERE rn = 1",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
WITH ranked AS (
    SELECT
        e.name,
        d.department_name,
        e.salary,
        e.hire_date,
        ROW_NUMBER() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC, e.hire_date ASC
        ) AS rn
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
)
SELECT name, department_name, salary, hire_date
FROM ranked
WHERE rn = 1
ORDER BY department_name;""",
        "order_matters": False,
        "explanation": (
            "**CTE (WITH clause)** defines a named temporary result set. "
            "The outer SELECT then filters it with WHERE rn = 1.\n\n"
            "**ROW_NUMBER()** assigns a unique integer to every row within each PARTITION. "
            "Unlike RANK() or DENSE_RANK(), ROW_NUMBER() never produces ties — "
            "if two employees are equally ranked, the tiebreaker (hire_date ASC) decides who gets rn=1.\n\n"
            "**PARTITION BY department_id** restarts numbering for each department.\n\n"
            "Results:\n"
            "- Engineering: Alice Johnson and Carol Williams both earn 95k, "
            "but Alice was hired 2020-01-15 vs Carol's 2021-07-01, so Alice gets rn=1.\n"
            "- Sales: David Brown and Frank Miller both earn 110k, "
            "Frank hired 2017-08-15, David 2018-11-10 → Frank gets rn=1.\n"
            "- Marketing: Henry Moore (78k, unique top salary) gets rn=1."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
WITH ranked AS (
    SELECT e.name, d.department_name, e.salary, e.hire_date,
        ROW_NUMBER() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC, e.hire_date ASC
        ) AS rn
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
)
SELECT name, department_name, salary, hire_date
FROM ranked WHERE rn = 1
ORDER BY department_name;""",
                "correct": True,
                "explanation": "CORRECT. CTE ranks employees within each department by salary (desc) then hire date (asc as tiebreaker). Outer query filters to rn=1 to get exactly one per department.",
            },
            {
                "id": "B",
                "text": """\
WITH ranked AS (
    SELECT e.name, d.department_name, e.salary, e.hire_date,
        RANK() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC
        ) AS rn
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
)
SELECT name, department_name, salary, hire_date
FROM ranked WHERE rn = 1
ORDER BY department_name;""",
                "correct": False,
                "explanation": "INCORRECT. Using RANK() without a tiebreaker means multiple employees with the same salary all get rn=1. The Engineering and Sales departments each have two employees with identical top salaries — this query returns 2 rows each instead of 1.",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name, d.department_name, e.salary, e.hire_date
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary = (
    SELECT MAX(salary) FROM employees e2
    WHERE e2.department_id = e.department_id
)
ORDER BY department_name;""",
                "correct": False,
                "explanation": "INCORRECT. The correlated subquery finds the max salary per department, but WHERE salary = MAX returns ALL employees at that max — still multiple rows per department when there are salary ties.",
            },
            {
                "id": "D",
                "text": """\
WITH ranked AS (
    SELECT e.name, d.department_name, e.salary, e.hire_date,
        ROW_NUMBER() OVER (
            ORDER BY e.salary DESC, e.hire_date ASC
        ) AS rn
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
)
SELECT name, department_name, salary, hire_date
FROM ranked WHERE rn = 1
ORDER BY department_name;""",
                "correct": False,
                "explanation": "INCORRECT. Missing PARTITION BY department_id — the window spans all employees globally, so rn=1 is the single highest-paid employee in the entire company, not one per department.",
            },
        ],
    },

    # ── 5 ────────────────────────────────────────────────────
    {
        "id": 5,
        "title": "Customers Who Have Never Placed an Order",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "The marketing team wants to re-engage inactive customers. "
            "Find every customer who has not placed any order at all. "
            "Two customers in the database (Oliver White and Sophia Harris) have never ordered."
        ),
        "question": (
            "Write a query that returns the name and city of every customer "
            "who has no orders in the orders table, ordered alphabetically by name."
        ),
        "hint": "Use LEFT JOIN from customers to orders, then filter WHERE order_id IS NULL. Alternatively use NOT IN or NOT EXISTS.",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
SELECT c.name AS customer_name, c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.name;""",
        "order_matters": False,
        "explanation": (
            "**LEFT JOIN** keeps all rows from the left table (customers) regardless of whether "
            "a match exists in orders. Where no order exists, all columns from orders are NULL.\n\n"
            "**WHERE o.order_id IS NULL** filters to only those unmatched customers.\n\n"
            "Alternative using NOT EXISTS:\n"
            "SELECT c.name, c.city FROM customers c\n"
            "WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)\n\n"
            "Alternative using NOT IN:\n"
            "SELECT name, city FROM customers\n"
            "WHERE customer_id NOT IN (SELECT customer_id FROM orders)\n\n"
            "All three are correct; LEFT JOIN + IS NULL and NOT EXISTS are generally more "
            "efficient than NOT IN on large datasets."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.name;""",
                "correct": True,
                "explanation": "CORRECT. LEFT JOIN retains all customers; IS NULL check on an orders column identifies those with no matching order.",
            },
            {
                "id": "B",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.name;""",
                "correct": False,
                "explanation": "INCORRECT. INNER JOIN only returns rows where a match exists — it discards customers with no orders before the WHERE clause even runs. o.order_id IS NULL will never be true after an INNER JOIN.",
            },
            {
                "id": "C",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
WHERE c.customer_id NOT IN (
    SELECT customer_id FROM orders
)
ORDER BY c.name;""",
                "correct": True,
                "explanation": "CORRECT (alternative). NOT IN subquery excludes customers whose ID appears in the orders table. Produces the same result as the LEFT JOIN approach.",
            },
            {
                "id": "D",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount = 0
ORDER BY c.name;""",
                "correct": False,
                "explanation": "INCORRECT. Filters for orders with a zero amount, not for customers with no orders at all. The NULL rows from the LEFT JOIN have NULL total_amount, not 0, so this query returns zero rows.",
            },
        ],
    },

    # ── 6 ────────────────────────────────────────────────────
    {
        "id": 6,
        "title": "Month-Over-Month Revenue Change with LAG",
        "difficulty": "Hard",
        "category": "Window Functions",
        "description": (
            "Finance tracks monthly revenue and wants to see how each month compares "
            "to the previous one. You have a monthly_revenue table spanning 2023-2024."
        ),
        "question": (
            "Write a query showing year, month, revenue, the previous month's revenue "
            "(aliased prev_revenue), and the absolute change (aliased revenue_change). "
            "The first row of the series should have NULL for prev_revenue and revenue_change. "
            "Order chronologically."
        ),
        "hint": "LAG(revenue) OVER (ORDER BY year, month) retrieves the value from the previous row in the specified order.",
        "tables": [MONTHLY_REVENUE],
        "correct_query": """\
SELECT
    year,
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY year, month) AS prev_revenue,
    revenue - LAG(revenue) OVER (ORDER BY year, month) AS revenue_change
FROM monthly_revenue
ORDER BY year, month;""",
        "order_matters": True,
        "explanation": (
            "**LAG(col) OVER (ORDER BY ...)** accesses the value of col from the row that "
            "comes immediately before the current row in the specified order. "
            "The very first row has no predecessor, so LAG returns NULL.\n\n"
            "**revenue - LAG(revenue) OVER (...)** subtracts to get the absolute change. "
            "When the previous value is NULL (first row), the subtraction also yields NULL.\n\n"
            "Key LAG syntax: LAG(value, offset, default) — offset defaults to 1 (one row back), "
            "default replaces NULL if you'd prefer 0 instead.\n\n"
            "**LEAD()** is the mirror: it looks forward to the next row instead of back."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT year, month, revenue,
    LAG(revenue) OVER (ORDER BY year, month) AS prev_revenue,
    revenue - LAG(revenue) OVER (ORDER BY year, month) AS revenue_change
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": True,
                "explanation": "CORRECT. LAG with no offset defaults to 1 row back, partitioned across the entire dataset ordered chronologically.",
            },
            {
                "id": "B",
                "text": """\
SELECT year, month, revenue,
    LAG(revenue, 1, 0) OVER (ORDER BY year, month) AS prev_revenue,
    revenue - LAG(revenue, 1, 0) OVER (ORDER BY year, month) AS revenue_change
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. The third argument '0' replaces NULL with 0 for the first row. This means the first row shows prev_revenue=0 and revenue_change=125000, but the problem requires NULL for the first row.",
            },
            {
                "id": "C",
                "text": """\
SELECT year, month, revenue,
    LEAD(revenue) OVER (ORDER BY year, month) AS prev_revenue,
    revenue - LEAD(revenue) OVER (ORDER BY year, month) AS revenue_change
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. LEAD() looks forward (next row), not backward. prev_revenue would contain the next month's revenue, and the last row would be NULL — the opposite of what is asked.",
            },
            {
                "id": "D",
                "text": """\
SELECT year, month, revenue,
    LAG(revenue) OVER (PARTITION BY year ORDER BY month) AS prev_revenue,
    revenue - LAG(revenue) OVER (PARTITION BY year ORDER BY month) AS revenue_change
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. PARTITION BY year restarts the window for each year, so January 2024 shows NULL for prev_revenue instead of December 2023's value. The December→January cross-year transition is lost.",
            },
        ],
    },

    # ── 7 ────────────────────────────────────────────────────
    {
        "id": 7,
        "title": "Full Department Roster Including Empty Departments",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "Management wants a summary of every department — including the HR department "
            "which currently has no employees. A simple INNER JOIN would silently drop it."
        ),
        "question": (
            "Write a query returning every department's name, location, employee count "
            "(aliased employee_count), and total salary payroll (aliased total_salary). "
            "Departments with no employees should show 0, not NULL. "
            "Order by employee_count descending, then department_name."
        ),
        "hint": "LEFT JOIN departments to employees (not the other way). Use COALESCE to replace NULL with 0. COUNT(e.employee_id) counts only non-NULL values.",
        "tables": [DEPARTMENTS, EMPLOYEES],
        "correct_query": """\
SELECT
    d.department_name,
    d.location,
    COUNT(e.employee_id)              AS employee_count,
    COALESCE(SUM(e.salary), 0)        AS total_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.location
ORDER BY employee_count DESC, d.department_name;""",
        "order_matters": False,
        "explanation": (
            "**LEFT JOIN** with departments on the left guarantees every department row "
            "appears in the result. For HR (no employees), the employees columns are NULL.\n\n"
            "**COUNT(e.employee_id)** — counting a specific column (not *) means NULL values "
            "(the HR rows) are NOT counted, correctly returning 0 for empty departments. "
            "COUNT(*) would return 1 for HR because there is still one row (filled with NULLs).\n\n"
            "**COALESCE(SUM(e.salary), 0)** — SUM of all NULLs is NULL, so COALESCE replaces "
            "it with 0 for the display.\n\n"
            "Note: FULL OUTER JOIN would also work here since all employees already belong to "
            "a department, but LEFT JOIN is cleaner and sufficient."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT d.department_name, d.location,
    COUNT(e.employee_id) AS employee_count,
    COALESCE(SUM(e.salary), 0) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.location
ORDER BY employee_count DESC, d.department_name;""",
                "correct": True,
                "explanation": "CORRECT. LEFT JOIN from departments ensures HR appears. COUNT on a nullable column and COALESCE handle the zero-employee case cleanly.",
            },
            {
                "id": "B",
                "text": """\
SELECT d.department_name, d.location,
    COUNT(*) AS employee_count,
    COALESCE(SUM(e.salary), 0) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.location
ORDER BY employee_count DESC, d.department_name;""",
                "correct": False,
                "explanation": "INCORRECT. COUNT(*) counts every row including the NULL-filled row for HR, so HR gets employee_count=1 instead of 0.",
            },
            {
                "id": "C",
                "text": """\
SELECT d.department_name, d.location,
    COUNT(e.employee_id) AS employee_count,
    COALESCE(SUM(e.salary), 0) AS total_salary
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.location
ORDER BY employee_count DESC, d.department_name;""",
                "correct": False,
                "explanation": "INCORRECT. The LEFT JOIN is reversed — employees is on the left, so only departments that have at least one employee are retained. HR vanishes from the result.",
            },
            {
                "id": "D",
                "text": """\
SELECT d.department_name, d.location,
    COUNT(e.employee_id) AS employee_count,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name, d.location
ORDER BY employee_count DESC, d.department_name;""",
                "correct": False,
                "explanation": "INCORRECT. Missing COALESCE — total_salary for HR shows NULL instead of 0. While not always wrong in practice, the problem explicitly asks for 0.",
            },
        ],
    },

    # ── 8 ────────────────────────────────────────────────────
    {
        "id": 8,
        "title": "Orders Above the Average Order Value",
        "difficulty": "Medium",
        "category": "Subqueries",
        "description": (
            "The logistics team flags high-value orders for priority handling. "
            "They define 'high value' as any order whose total exceeds the overall average "
            "order value across all orders."
        ),
        "question": (
            "Write a query returning the order_id, customer name, order_date, and "
            "total_amount for every order above the average order value. "
            "Include the average (rounded to 2 decimals, aliased avg_order_value) in each result row. "
            "Order by total_amount descending."
        ),
        "hint": "Use a scalar subquery (SELECT AVG(total_amount) FROM orders) in both the WHERE clause and the SELECT list.",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
SELECT
    o.order_id,
    c.name  AS customer_name,
    o.order_date,
    o.total_amount,
    ROUND((SELECT AVG(total_amount) FROM orders), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.total_amount > (SELECT AVG(total_amount) FROM orders)
ORDER BY o.total_amount DESC;""",
        "order_matters": False,
        "explanation": (
            "A **scalar subquery** returns a single value and can be used anywhere a literal "
            "value is valid — in SELECT, WHERE, HAVING, etc.\n\n"
            "(SELECT AVG(total_amount) FROM orders) computes the mean of all 20 orders "
            "(≈ 482.13). The WHERE clause uses this as a filter threshold.\n\n"
            "The same subquery in SELECT shows the average alongside each qualifying row — "
            "useful for context without a JOIN.\n\n"
            "Alternative using a derived table in FROM:\n"
            "FROM orders o, (SELECT ROUND(AVG(total_amount),2) AS avg_val FROM orders) avg_t\n"
            "WHERE o.total_amount > avg_t.avg_val"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT o.order_id, c.name AS customer_name, o.order_date,
    o.total_amount,
    ROUND((SELECT AVG(total_amount) FROM orders), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.total_amount > (SELECT AVG(total_amount) FROM orders)
ORDER BY o.total_amount DESC;""",
                "correct": True,
                "explanation": "CORRECT. Scalar subquery computes the overall average; the WHERE clause filters rows above it; the SELECT clause shows the average per row for context.",
            },
            {
                "id": "B",
                "text": """\
SELECT o.order_id, c.name AS customer_name, o.order_date,
    o.total_amount,
    ROUND(AVG(o.total_amount), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.total_amount > AVG(o.total_amount)
ORDER BY o.total_amount DESC;""",
                "correct": False,
                "explanation": "INCORRECT. AVG() is an aggregate function and cannot be used in a WHERE clause directly. This raises a syntax/semantic error.",
            },
            {
                "id": "C",
                "text": """\
SELECT o.order_id, c.name AS customer_name, o.order_date,
    o.total_amount,
    ROUND(avg_t.avg_val, 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
CROSS JOIN (SELECT AVG(total_amount) AS avg_val FROM orders) avg_t
WHERE o.total_amount > avg_t.avg_val
ORDER BY o.total_amount DESC;""",
                "correct": True,
                "explanation": "CORRECT (alternative). CROSS JOIN with a single-row derived table is another valid pattern. Because avg_t always has exactly one row, CROSS JOIN is equivalent to the scalar subquery approach.",
            },
            {
                "id": "D",
                "text": """\
SELECT o.order_id, c.name AS customer_name, o.order_date,
    o.total_amount,
    ROUND((SELECT AVG(total_amount) FROM orders), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
HAVING o.total_amount > (SELECT AVG(total_amount) FROM orders)
ORDER BY o.total_amount DESC;""",
                "correct": False,
                "explanation": "INCORRECT. HAVING without GROUP BY applies a condition after all rows are consolidated into one group — only one row total would be returned. Row-level filtering belongs in WHERE, not HAVING.",
            },
        ],
    },

    # ── 9 ────────────────────────────────────────────────────
    {
        "id": 9,
        "title": "Cumulative Revenue Running Total by Year",
        "difficulty": "Hard",
        "category": "Window Functions",
        "description": (
            "The CFO wants a month-by-month view with two running totals: "
            "one that resets at the start of each year (year-to-date), "
            "and one that accumulates across all time (all-time cumulative). "
            "Both should be computed without GROUP BY — use window functions."
        ),
        "question": (
            "Write a query showing year, month, revenue, "
            "a year-to-date running total (aliased ytd_revenue) that resets each January, "
            "and an all-time cumulative total (aliased all_time_cumulative). "
            "Order chronologically."
        ),
        "hint": "For YTD: SUM(revenue) OVER (PARTITION BY year ORDER BY month). For all-time: SUM(revenue) OVER (ORDER BY year, month).",
        "tables": [MONTHLY_REVENUE],
        "correct_query": """\
SELECT
    year,
    month,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY year
        ORDER BY month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS ytd_revenue,
    SUM(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS all_time_cumulative
FROM monthly_revenue
ORDER BY year, month;""",
        "order_matters": True,
        "explanation": (
            "**SUM() OVER (PARTITION BY year ORDER BY month)** — PARTITION BY year means the "
            "running sum resets to zero at the start of each new year (year-to-date).\n\n"
            "**SUM() OVER (ORDER BY year, month)** — no PARTITION means the sum spans the "
            "entire table in chronological order (all-time cumulative).\n\n"
            "**ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW** is the explicit frame "
            "clause; when ORDER BY is present the default frame is already "
            "RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, which is equivalent for "
            "unique sort keys. Making it explicit with ROWS is clearer and avoids subtle "
            "differences when there are duplicate sort key values.\n\n"
            "This pattern is the foundation for any running-total or moving-average calculation."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT year, month, revenue,
    SUM(revenue) OVER (
        PARTITION BY year ORDER BY month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS ytd_revenue,
    SUM(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS all_time_cumulative
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": True,
                "explanation": "CORRECT. PARTITION BY year resets the YTD window each year; no partition on all_time gives the global cumulative. Explicit ROWS frame is best practice.",
            },
            {
                "id": "B",
                "text": """\
SELECT year, month, revenue,
    SUM(revenue) OVER (PARTITION BY year ORDER BY month) AS ytd_revenue,
    SUM(revenue) OVER (ORDER BY year, month) AS all_time_cumulative
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": True,
                "explanation": "CORRECT. Omitting the ROWS frame clause uses the default RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, which produces identical results for unique (year, month) combinations.",
            },
            {
                "id": "C",
                "text": """\
SELECT year, month, revenue,
    SUM(revenue) OVER (ORDER BY month) AS ytd_revenue,
    SUM(revenue) OVER (ORDER BY year, month) AS all_time_cumulative
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. ytd_revenue uses ORDER BY month without PARTITION BY year — the window is not reset per year. January 2024 would accumulate on top of all 2023 months instead of starting fresh.",
            },
            {
                "id": "D",
                "text": """\
SELECT year, month, revenue,
    SUM(revenue) OVER (PARTITION BY year) AS ytd_revenue,
    SUM(revenue) OVER () AS all_time_cumulative
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. Missing ORDER BY inside the windows. Without ORDER BY, SUM() OVER (...) computes the total for the entire partition (or entire table), not a running total. Every month in 2023 gets the same 2023 total instead of a cumulative figure.",
            },
        ],
    },

    # ── 10 ───────────────────────────────────────────────────
    {
        "id": 10,
        "title": "Revenue Share by Product Category",
        "difficulty": "Hard",
        "category": "Joins",
        "description": (
            "The product team wants to understand which categories drive the most revenue. "
            "You have three tables: order_items (line-level), products (with category), "
            "and orders. Calculate revenue as quantity × unit_price from order_items."
        ),
        "question": (
            "Write a query showing each product category, the number of distinct products sold "
            "(aliased products_sold), total revenue (quantity × unit_price, aliased total_revenue, "
            "rounded to 2 decimals), and that category's percentage of all revenue "
            "(aliased revenue_pct, rounded to 1 decimal). "
            "Order by total_revenue descending."
        ),
        "hint": "JOIN order_items to products. Use SUM(oi.quantity * oi.unit_price) for revenue. For percentage: revenue / SUM(revenue) OVER () * 100 as a window function.",
        "tables": [ORDER_ITEMS, PRODUCTS, ORDERS],
        "correct_query": """\
SELECT
    p.category,
    COUNT(DISTINCT p.product_id)                                 AS products_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2)                  AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price) * 100.0
        / SUM(SUM(oi.quantity * oi.unit_price)) OVER ()
    , 1)                                                         AS revenue_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;""",
        "order_matters": False,
        "explanation": (
            "**JOIN order_items to products** links each line item to its category.\n\n"
            "**SUM(quantity * unit_price)** calculates actual revenue from the line items "
            "(not from orders.total_amount, which is redundant here).\n\n"
            "**SUM(SUM(...)) OVER ()** — a window function applied to an aggregate. "
            "The inner SUM aggregates within each GROUP BY category; "
            "the outer SUM() OVER () sums those group-level values across all groups, "
            "giving the grand total. Dividing the category total by the grand total × 100 "
            "yields the percentage share.\n\n"
            "Results (approximate):\n"
            "- Electronics: ~77.8% of revenue\n"
            "- Furniture: ~21.1%\n"
            "- Stationery: ~1.1%"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT p.category,
    COUNT(DISTINCT p.product_id) AS products_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price) * 100.0
        / SUM(SUM(oi.quantity * oi.unit_price)) OVER ()
    , 1) AS revenue_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;""",
                "correct": True,
                "explanation": "CORRECT. Aggregates revenue per category, then uses SUM(SUM(...)) OVER () — a window over the aggregated result — to compute each category's share of the grand total.",
            },
            {
                "id": "B",
                "text": """\
SELECT p.category,
    COUNT(DISTINCT p.product_id) AS products_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price) * 100.0
        / (SELECT SUM(quantity * unit_price) FROM order_items)
    , 1) AS revenue_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;""",
                "correct": True,
                "explanation": "CORRECT (alternative). A scalar subquery computes the grand total. This is equivalent to the SUM(SUM()) OVER () window approach and produces the same percentages.",
            },
            {
                "id": "C",
                "text": """\
SELECT p.category,
    COUNT(DISTINCT p.product_id) AS products_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price) * 100.0
        / SUM(oi.quantity * oi.unit_price) OVER ()
    , 1) AS revenue_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;""",
                "correct": False,
                "explanation": "INCORRECT. SUM(oi.quantity * oi.unit_price) OVER () applies the window to the un-aggregated rows — this is invalid inside a query that already has GROUP BY, or at best gives wrong values because the window sees raw rows, not grouped totals.",
            },
            {
                "id": "D",
                "text": """\
SELECT p.category,
    COUNT(p.product_id) AS products_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price) * 100.0
        / SUM(SUM(oi.quantity * oi.unit_price)) OVER ()
    , 1) AS revenue_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;""",
                "correct": False,
                "explanation": "INCORRECT. COUNT(p.product_id) counts every order-item row (including duplicates of the same product across orders), not the count of distinct products sold. COUNT(DISTINCT p.product_id) is required.",
            },
        ],
    },

    # ── 11 ───────────────────────────────────────────────────
    {
        "id": 11,
        "title": "High-Volume Customers Using HAVING",
        "difficulty": "Medium",
        "category": "Aggregation & Grouping",
        "description": (
            "The loyalty team wants to identify frequent buyers — customers who have "
            "placed three or more orders. HAVING is the SQL clause designed for filtering "
            "on aggregate results after GROUP BY."
        ),
        "question": (
            "Write a query returning the name and order count of every customer who has "
            "placed 3 or more orders. Alias the count as order_count. "
            "Order by order_count descending, then alphabetically by name."
        ),
        "hint": "JOIN customers to orders, GROUP BY customer, then use HAVING COUNT(order_id) >= 3.",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
SELECT
    c.name AS customer_name,
    COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) >= 3
ORDER BY order_count DESC, customer_name;""",
        "order_matters": False,
        "explanation": (
            "**WHERE** filters individual rows before aggregation — you cannot reference "
            "aggregate functions there.\n\n"
            "**HAVING** filters after GROUP BY, operating on the grouped result. "
            "It can reference aggregate expressions like COUNT(), SUM(), AVG().\n\n"
            "You can also write HAVING COUNT(*) >= 3 here since the JOIN guarantees no NULL "
            "order rows, but COUNT(o.order_id) is more explicit and resilient.\n\n"
            "Results: Alice Chen (4 orders), Bob Martinez (3), Carol Lee (3)."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT c.name AS customer_name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) >= 3
ORDER BY order_count DESC, customer_name;""",
                "correct": True,
                "explanation": "CORRECT. GROUP BY collapses rows per customer; HAVING filters to those with 3+ orders.",
            },
            {
                "id": "B",
                "text": """\
SELECT c.name AS customer_name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE COUNT(o.order_id) >= 3
GROUP BY c.customer_id, c.name
ORDER BY order_count DESC, customer_name;""",
                "correct": False,
                "explanation": "INCORRECT. Aggregate functions (COUNT, SUM, AVG…) cannot appear in a WHERE clause — they are evaluated after rows are grouped. This raises a syntax error.",
            },
            {
                "id": "C",
                "text": """\
SELECT c.name AS customer_name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING order_count >= 3
ORDER BY order_count DESC, customer_name;""",
                "correct": False,
                "explanation": "INCORRECT. Most SQL dialects (including standard PostgreSQL) do not allow referencing a SELECT alias (order_count) inside HAVING — HAVING is evaluated before SELECT aliasing. Use the full expression: HAVING COUNT(o.order_id) >= 3.",
            },
            {
                "id": "D",
                "text": """\
SELECT c.name AS customer_name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
HAVING COUNT(o.order_id) >= 3
ORDER BY order_count DESC, customer_name;""",
                "correct": False,
                "explanation": "INCORRECT. HAVING without GROUP BY treats all rows as a single group, returning at most one row for the entire table — not per customer.",
            },
        ],
    },

    # ── 12 ───────────────────────────────────────────────────
    {
        "id": 12,
        "title": "Salary Quartiles with NTILE",
        "difficulty": "Medium",
        "category": "Window Functions",
        "description": (
            "Compensation analysis often buckets employees into quartiles "
            "(four equal-sized groups) based on salary. NTILE(n) distributes rows "
            "as evenly as possible into n buckets in the order you specify."
        ),
        "question": (
            "Write a query assigning each employee to a salary quartile (1 = lowest 25%, "
            "4 = highest 25%). Include employee name, department name, salary, and the quartile "
            "number aliased as salary_quartile. Order by salary ascending, then name ascending."
        ),
        "hint": "NTILE(4) OVER (ORDER BY salary ASC, name ASC) puts the lowest earners in Q1.",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
SELECT
    e.name,
    d.department_name,
    e.salary,
    NTILE(4) OVER (ORDER BY e.salary ASC, e.name ASC) AS salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary ASC, e.name ASC;""",
        "order_matters": False,
        "explanation": (
            "**NTILE(4)** divides the ordered result into 4 buckets as evenly as possible. "
            "With 10 employees and 4 buckets: the first 2 buckets get 3 rows each, "
            "the last 2 get 2 rows each (10 = 3+3+2+2).\n\n"
            "**ORDER BY salary ASC** ensures the lowest-paid employees land in quartile 1. "
            "Adding **name ASC** as a tiebreaker makes the assignment deterministic when "
            "two employees share the same salary.\n\n"
            "Result buckets:\n"
            "- Q1 (lowest): Grace, Isabel, James (all 72k–75k)\n"
            "- Q2: Henry, Bob, Alice (78k–95k)\n"
            "- Q3: Carol, Emma (95k–98k)\n"
            "- Q4 (highest): David, Frank (both 110k)"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    NTILE(4) OVER (ORDER BY e.salary ASC, e.name ASC) AS salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary ASC, e.name ASC;""",
                "correct": True,
                "explanation": "CORRECT. NTILE(4) with ASC salary order places lowest earners in Q1. Name tiebreaker ensures deterministic bucket assignment.",
            },
            {
                "id": "B",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    NTILE(4) OVER (ORDER BY e.salary DESC) AS salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary ASC, e.name ASC;""",
                "correct": False,
                "explanation": "INCORRECT. ORDER BY salary DESC assigns Q1 to the highest-paid employees — the opposite of what is asked.",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    NTILE(4) OVER (PARTITION BY e.department_id ORDER BY e.salary ASC) AS salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary ASC, e.name ASC;""",
                "correct": False,
                "explanation": "INCORRECT. PARTITION BY department_id assigns quartiles within each department separately. Engineering, Sales, and Marketing each get their own Q1–Q4, which is not a company-wide quartile ranking.",
            },
            {
                "id": "D",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    NTILE(3) OVER (ORDER BY e.salary ASC, e.name ASC) AS salary_quartile
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary ASC, e.name ASC;""",
                "correct": False,
                "explanation": "INCORRECT. NTILE(3) creates tertiles (3 buckets), not quartiles. The alias salary_quartile is misleading since only groups 1–3 exist.",
            },
        ],
    },

    # ── 13 ───────────────────────────────────────────────────
    {
        "id": 13,
        "title": "Department Max Salary vs Individual Using FIRST_VALUE",
        "difficulty": "Medium",
        "category": "Window Functions",
        "description": (
            "FIRST_VALUE() lets you reference the first row in a window partition — "
            "ideal for comparing each row to the 'leader' in its group. "
            "Use it here to show how far each employee's salary is from the top earner "
            "in their department."
        ),
        "question": (
            "Write a query showing each employee's name, department name, salary, "
            "the highest salary in their department (aliased dept_max_salary), "
            "and the gap between that max and their salary (aliased gap_from_max). "
            "Order by department name, then salary descending."
        ),
        "hint": "FIRST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) gives the highest salary in each department.",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
SELECT
    e.name,
    d.department_name,
    e.salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
    ) AS dept_max_salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
    ) - e.salary AS gap_from_max
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC, e.name;""",
        "order_matters": False,
        "explanation": (
            "**FIRST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC)** "
            "returns the value from the first row in each partition — with ORDER BY salary DESC "
            "that first row is the highest earner in the department.\n\n"
            "**LAST_VALUE()** would give the minimum (last row in the ordered window), "
            "but note that the default frame RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW "
            "means LAST_VALUE only sees rows up to the current one, not all partition rows.\n\n"
            "The gap column shows 0 for the top earners (they compare to themselves) and "
            "positive values for everyone else."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
    ) AS dept_max_salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
    ) - e.salary AS gap_from_max
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC, e.name;""",
                "correct": True,
                "explanation": "CORRECT. FIRST_VALUE with PARTITION BY dept and ORDER BY salary DESC picks the department's top earner for every row in that partition.",
            },
            {
                "id": "B",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    FIRST_VALUE(e.salary) OVER (ORDER BY e.salary DESC) AS dept_max_salary,
    FIRST_VALUE(e.salary) OVER (ORDER BY e.salary DESC) - e.salary AS gap_from_max
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC, e.name;""",
                "correct": False,
                "explanation": "INCORRECT. Missing PARTITION BY — without it the window covers all employees, so dept_max_salary is the global top salary (110k) for every row, not the per-department max.",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    LAST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS dept_max_salary,
    LAST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) - e.salary AS gap_from_max
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC, e.name;""",
                "correct": False,
                "explanation": "INCORRECT. LAST_VALUE with this frame gives the minimum salary in the partition (last row in DESC order = lowest salary). gap_from_max would be negative for most employees.",
            },
            {
                "id": "D",
                "text": """\
SELECT e.name, d.department_name, e.salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary ASC
    ) AS dept_max_salary,
    FIRST_VALUE(e.salary) OVER (
        PARTITION BY e.department_id ORDER BY e.salary ASC
    ) - e.salary AS gap_from_max
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_name, e.salary DESC, e.name;""",
                "correct": False,
                "explanation": "INCORRECT. ORDER BY salary ASC means FIRST_VALUE returns the minimum salary in the partition, not the maximum. The result would show negative gaps for higher earners.",
            },
        ],
    },

    # ── 14 ───────────────────────────────────────────────────
    {
        "id": 14,
        "title": "3-Month Moving Average of Revenue",
        "difficulty": "Medium",
        "category": "Window Functions",
        "description": (
            "A 3-month trailing moving average smooths out spikes in revenue data, "
            "making trends easier to spot. The ROWS BETWEEN frame clause controls exactly "
            "which rows are included in each window calculation."
        ),
        "question": (
            "Write a query showing year, month, revenue, and the 3-month trailing moving average "
            "(current month plus the two preceding months). "
            "Alias it as moving_avg_3m and round to 2 decimal places. Order chronologically."
        ),
        "hint": "AVG(revenue) OVER (ORDER BY year, month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)",
        "tables": [MONTHLY_REVENUE],
        "correct_query": """\
SELECT
    year,
    month,
    revenue,
    ROUND(AVG(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_3m
FROM monthly_revenue
ORDER BY year, month;""",
        "order_matters": True,
        "explanation": (
            "**ROWS BETWEEN 2 PRECEDING AND CURRENT ROW** includes the current row and the "
            "two rows immediately before it in the ORDER BY sequence — a 3-row (3-month) window.\n\n"
            "For the first two rows the window is smaller (1 and 2 rows respectively), "
            "so the average is computed on fewer data points.\n\n"
            "**RANGE vs ROWS**: RANGE is the default frame when ORDER BY is present. "
            "ROWS counts actual row positions; RANGE groups rows with identical sort key values. "
            "For unique (year, month) pairs they are equivalent — but ROWS is safer and clearer.\n\n"
            "A centered moving average would use ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT year, month, revenue,
    ROUND(AVG(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_3m
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": True,
                "explanation": "CORRECT. ROWS BETWEEN 2 PRECEDING AND CURRENT ROW creates a trailing 3-month window.",
            },
            {
                "id": "B",
                "text": """\
SELECT year, month, revenue,
    ROUND(AVG(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ), 2) AS moving_avg_3m
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING is a centered 3-month window (previous, current, next). The question asks for a trailing average (current and 2 before).",
            },
            {
                "id": "C",
                "text": """\
SELECT year, month, revenue,
    ROUND(AVG(revenue) OVER (
        PARTITION BY year
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_3m
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. PARTITION BY year resets the window at the start of each year, so January 2024 cannot include Nov/Dec 2023 in its 3-month average. The cross-year average is incorrect.",
            },
            {
                "id": "D",
                "text": """\
SELECT year, month, revenue,
    ROUND(AVG(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_3m
FROM monthly_revenue
ORDER BY year, month;""",
                "correct": False,
                "explanation": "INCORRECT. UNBOUNDED PRECEDING includes all rows from the start of the dataset, producing a cumulative average — not a 3-month window.",
            },
        ],
    },

    # ── 15 ───────────────────────────────────────────────────
    {
        "id": 15,
        "title": "Manager-Employee Hierarchy via Self-Join",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "When a table has a self-referencing foreign key (manager_id → staff_id), "
            "you can join the table to itself using two aliases to connect employees "
            "to their direct managers."
        ),
        "question": (
            "Using the staff table, write a query that shows each employee's name, "
            "their manager's name (aliased manager_name), their department, "
            "and their salary. Exclude the CEO (who has no manager). "
            "Order results alphabetically by employee name."
        ),
        "hint": "JOIN staff AS e to staff AS m ON e.manager_id = m.staff_id. INNER JOIN naturally excludes NULL manager_id rows.",
        "tables": [STAFF],
        "correct_query": """\
SELECT
    e.name     AS employee_name,
    m.name     AS manager_name,
    e.department,
    e.salary
FROM staff e
JOIN staff m ON e.manager_id = m.staff_id
ORDER BY e.name;""",
        "order_matters": False,
        "explanation": (
            "**Self-join**: the staff table is joined to itself using two aliases (e = employee, "
            "m = manager). The join condition e.manager_id = m.staff_id links each person to their boss.\n\n"
            "**INNER JOIN** automatically excludes Sarah Connor because her manager_id is NULL — "
            "NULL does not equal any staff_id, so the join finds no match for her row.\n\n"
            "**LEFT JOIN** would keep Sarah Connor with NULL in the manager_name column — "
            "useful if you want to see the full org chart including the CEO."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT e.name AS employee_name, m.name AS manager_name,
    e.department, e.salary
FROM staff e
JOIN staff m ON e.manager_id = m.staff_id
ORDER BY e.name;""",
                "correct": True,
                "explanation": "CORRECT. Self-join with INNER JOIN links each employee to their manager and naturally excludes the CEO (NULL manager_id).",
            },
            {
                "id": "B",
                "text": """\
SELECT e.name AS employee_name, m.name AS manager_name,
    e.department, e.salary
FROM staff e
LEFT JOIN staff m ON e.manager_id = m.staff_id
ORDER BY e.name;""",
                "correct": False,
                "explanation": "INCORRECT. LEFT JOIN includes Sarah Connor with manager_name = NULL. The question says to exclude the CEO, so INNER JOIN is required.",
            },
            {
                "id": "C",
                "text": """\
SELECT e.name AS employee_name, m.name AS manager_name,
    e.department, e.salary
FROM staff e
JOIN staff m ON m.manager_id = e.staff_id
ORDER BY e.name;""",
                "correct": False,
                "explanation": "INCORRECT. The join condition is reversed — m.manager_id = e.staff_id finds employees who are managed by someone else, essentially returning managers with their direct reports swapped.",
            },
            {
                "id": "D",
                "text": """\
SELECT e.name AS employee_name, m.name AS manager_name,
    e.department, e.salary
FROM staff e, staff m
WHERE e.manager_id = m.staff_id
    AND e.manager_id IS NOT NULL
ORDER BY e.name;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Old-style implicit JOIN syntax with an explicit IS NOT NULL filter produces the same result — though explicit JOIN syntax (choice A) is preferred for clarity.",
            },
        ],
    },

    # ── 16 ───────────────────────────────────────────────────
    {
        "id": 16,
        "title": "Categorizing Orders with CASE WHEN",
        "difficulty": "Medium",
        "category": "Aggregation & Grouping",
        "description": (
            "CASE WHEN inside aggregation lets you group and summarize data by a computed "
            "category rather than an existing column. Here you'll segment orders into "
            "value tiers and calculate metrics for each."
        ),
        "question": (
            "Write a query that buckets each order into 'High' (total_amount >= 500), "
            "'Medium' (>= 100 and < 500), or 'Low' (< 100). "
            "For each tier show the tier name (aliased value_tier), order count "
            "(aliased order_count), and total revenue (aliased total_revenue, rounded to 2 decimals). "
            "Order by total_revenue descending."
        ),
        "hint": "CASE WHEN ... END in the SELECT and GROUP BY. Use the same CASE expression in GROUP BY.",
        "tables": [ORDERS],
        "correct_query": """\
SELECT
    CASE
        WHEN total_amount >= 500 THEN 'High'
        WHEN total_amount >= 100 THEN 'Medium'
        ELSE 'Low'
    END AS value_tier,
    COUNT(*) AS order_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM orders
GROUP BY value_tier
ORDER BY total_revenue DESC;""",
        "order_matters": False,
        "explanation": (
            "**CASE WHEN** is evaluated row-by-row: if total_amount >= 500 → 'High'; "
            "else if >= 100 → 'Medium'; else → 'Low'. "
            "Conditions are checked in order — once one matches, the rest are skipped.\n\n"
            "**GROUP BY value_tier** (using the alias) works in DuckDB/PostgreSQL because "
            "GROUP BY is processed after the SELECT clause aliases are defined. "
            "Alternatively you can repeat the full CASE expression in GROUP BY.\n\n"
            "Results: High (6 orders, $6,299.94), Medium (12 orders, $3,182.71), "
            "Low (2 orders, $159.97)."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT
    CASE WHEN total_amount >= 500 THEN 'High'
         WHEN total_amount >= 100 THEN 'Medium'
         ELSE 'Low' END AS value_tier,
    COUNT(*) AS order_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM orders
GROUP BY value_tier
ORDER BY total_revenue DESC;""",
                "correct": True,
                "explanation": "CORRECT. CASE WHEN creates the tier label per row; GROUP BY aggregates by tier. ORDER BY total_revenue DESC sorts High first.",
            },
            {
                "id": "B",
                "text": """\
SELECT
    CASE WHEN total_amount >= 100 THEN 'Medium'
         WHEN total_amount >= 500 THEN 'High'
         ELSE 'Low' END AS value_tier,
    COUNT(*) AS order_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM orders
GROUP BY value_tier
ORDER BY total_revenue DESC;""",
                "correct": False,
                "explanation": "INCORRECT. The CASE conditions are in the wrong order. Since >= 100 is checked first, a $600 order matches 'Medium' before it ever reaches the 'High' condition — all orders >= $100 become 'Medium'.",
            },
            {
                "id": "C",
                "text": """\
SELECT
    CASE WHEN total_amount >= 500 THEN 'High'
         WHEN total_amount >= 100 THEN 'Medium'
         ELSE 'Low' END AS value_tier,
    COUNT(*) AS order_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM orders
GROUP BY order_id
ORDER BY total_revenue DESC;""",
                "correct": False,
                "explanation": "INCORRECT. GROUP BY order_id produces one row per order rather than per tier — the CASE label is there but never actually aggregated.",
            },
            {
                "id": "D",
                "text": """\
SELECT
    CASE WHEN total_amount >= 500 THEN 'High'
         WHEN total_amount >= 100 THEN 'Medium'
         ELSE 'Low' END AS value_tier,
    COUNT(*) AS order_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM orders
ORDER BY total_revenue DESC;""",
                "correct": False,
                "explanation": "INCORRECT. Missing GROUP BY entirely — without it the query is ambiguous (aggregate functions mixed with a non-aggregated CASE expression).",
            },
        ],
    },

    # ── 17 ───────────────────────────────────────────────────
    {
        "id": 17,
        "title": "Customers with a High-Value Order Using EXISTS",
        "difficulty": "Medium",
        "category": "Subqueries",
        "description": (
            "EXISTS is a semi-join pattern: it returns TRUE if a correlated subquery "
            "finds at least one matching row, without materialising the full join result. "
            "It stops searching as soon as one match is found, making it efficient."
        ),
        "question": (
            "Write a query returning the name and city of every customer who has placed "
            "at least one order with a total_amount greater than $400. "
            "Order alphabetically by customer name."
        ),
        "hint": "WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id AND o.total_amount > 400)",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
SELECT c.name AS customer_name, c.city
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
      AND o.total_amount > 400
)
ORDER BY c.name;""",
        "order_matters": False,
        "explanation": (
            "**EXISTS** evaluates the correlated subquery once per outer row. "
            "If any matching order is found, the customer row is included. "
            "SELECT 1 (or SELECT *) is conventional — only the existence of a row matters, "
            "not the values returned.\n\n"
            "Qualifying customers (those with at least one order > $400):\n"
            "Alice Chen (orders: $1299.99, $429.98), Carol Lee ($549.99), "
            "David Kim ($1299.99), Emma Rodriguez ($1299.99), "
            "Henry Davis ($549.99), Isabel Wilson ($1299.99).\n\n"
            "NOT EXISTS is the inverse: it returns customers with no orders above $400."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id AND o.total_amount > 400
)
ORDER BY c.name;""",
                "correct": True,
                "explanation": "CORRECT. EXISTS with a correlated subquery filters to customers who have at least one qualifying order.",
            },
            {
                "id": "B",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id AND o.total_amount > 400
)
ORDER BY c.name;""",
                "correct": False,
                "explanation": "INCORRECT. NOT EXISTS returns the opposite — customers who have NO orders above $400.",
            },
            {
                "id": "C",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount > 400
ORDER BY c.name;""",
                "correct": False,
                "explanation": "INCORRECT. This JOIN returns a row per qualifying order, so a customer with 3 orders > $400 appears 3 times. DISTINCT would fix duplicates but EXISTS is semantically cleaner.",
            },
            {
                "id": "D",
                "text": """\
SELECT c.name AS customer_name, c.city
FROM customers c
WHERE c.customer_id IN (
    SELECT customer_id FROM orders WHERE total_amount > 400
)
ORDER BY c.name;""",
                "correct": True,
                "explanation": "CORRECT (alternative). IN with a subquery is semantically equivalent to EXISTS here and produces the same result.",
            },
        ],
    },

    # ── 18 ───────────────────────────────────────────────────
    {
        "id": 18,
        "title": "High Average-Salary Departments via Derived Table",
        "difficulty": "Medium",
        "category": "Subqueries",
        "description": (
            "A derived table (inline subquery in the FROM clause) lets you pre-aggregate "
            "data and then filter or join on those aggregated results — "
            "similar to a CTE but written directly in-line."
        ),
        "question": (
            "Using a derived table (subquery in FROM), write a query that returns the "
            "department name, average salary (aliased avg_salary, rounded to 2 decimals), "
            "and employee count (aliased employee_count) for departments "
            "where the average salary exceeds $85,000. Order by avg_salary descending."
        ),
        "hint": "FROM departments d JOIN (SELECT department_id, ROUND(AVG(salary),2) AS avg_salary, COUNT(*) AS employee_count FROM employees GROUP BY department_id) AS stats ON ...",
        "tables": [EMPLOYEES, DEPARTMENTS],
        "correct_query": """\
SELECT
    d.department_name,
    stats.avg_salary,
    stats.employee_count
FROM departments d
JOIN (
    SELECT
        department_id,
        ROUND(AVG(salary), 2) AS avg_salary,
        COUNT(*)              AS employee_count
    FROM employees
    GROUP BY department_id
) AS stats ON d.department_id = stats.department_id
WHERE stats.avg_salary > 85000
ORDER BY stats.avg_salary DESC;""",
        "order_matters": False,
        "explanation": (
            "A **derived table** is a subquery in the FROM clause given an alias (here: stats). "
            "The database executes it once and treats the result like a regular table.\n\n"
            "Department averages:\n"
            "- Sales: (110k+98k+110k)/3 = $106,000 → qualifies\n"
            "- Engineering: (95k+85k+95k+75k)/4 = $87,500 → qualifies\n"
            "- Marketing: (72k+78k+72k)/3 = $74,000 → excluded\n"
            "- HR: no employees → not in derived table\n\n"
            "A CTE (WITH stats AS (...) SELECT ...) is functionally identical "
            "but separates the subquery for readability."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT d.department_name, stats.avg_salary, stats.employee_count
FROM departments d
JOIN (
    SELECT department_id,
        ROUND(AVG(salary), 2) AS avg_salary,
        COUNT(*) AS employee_count
    FROM employees
    GROUP BY department_id
) AS stats ON d.department_id = stats.department_id
WHERE stats.avg_salary > 85000
ORDER BY stats.avg_salary DESC;""",
                "correct": True,
                "explanation": "CORRECT. Derived table aggregates per department; outer query filters and joins to get department names.",
            },
            {
                "id": "B",
                "text": """\
SELECT d.department_name,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    COUNT(e.employee_id) AS employee_count
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING ROUND(AVG(e.salary), 2) > 85000
ORDER BY avg_salary DESC;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Using HAVING on the grouped result achieves the same filter without a derived table. Both approaches are valid.",
            },
            {
                "id": "C",
                "text": """\
SELECT d.department_name, stats.avg_salary, stats.employee_count
FROM departments d
JOIN (
    SELECT department_id,
        ROUND(AVG(salary), 2) AS avg_salary,
        COUNT(*) AS employee_count
    FROM employees
    GROUP BY department_id
) AS stats ON d.department_id = stats.department_id
WHERE AVG(salary) > 85000
ORDER BY stats.avg_salary DESC;""",
                "correct": False,
                "explanation": "INCORRECT. WHERE AVG(salary) is invalid — aggregate functions cannot be used in WHERE. The alias stats.avg_salary must be referenced instead.",
            },
            {
                "id": "D",
                "text": """\
SELECT d.department_name, stats.avg_salary, stats.employee_count
FROM departments d
JOIN (
    SELECT department_id,
        ROUND(AVG(salary), 2) AS avg_salary,
        COUNT(*) AS employee_count
    FROM employees
) AS stats ON d.department_id = stats.department_id
WHERE stats.avg_salary > 85000
ORDER BY stats.avg_salary DESC;""",
                "correct": False,
                "explanation": "INCORRECT. The derived table is missing GROUP BY department_id, so AVG() computes a single overall average across all employees — producing one row, not one per department.",
            },
        ],
    },

    # ── 19 ───────────────────────────────────────────────────
    {
        "id": 19,
        "title": "Multiple Chained CTEs for Customer Analysis",
        "difficulty": "Medium",
        "category": "CTEs (Common Table Expressions)",
        "description": (
            "Multiple CTEs can be chained in a single WITH clause, with later CTEs "
            "referencing earlier ones. This keeps complex logic readable and avoids "
            "deeply nested subqueries."
        ),
        "question": (
            "Using two CTEs — one for total spend per customer, one for order count — "
            "write a query returning customers whose total_spent exceeds $500 AND "
            "who have 2 or more orders. Show customer name, total_spent (rounded to 2 decimals), "
            "and order_count. Order by total_spent descending."
        ),
        "hint": "WITH totals AS (SELECT customer_id, SUM(...)), counts AS (SELECT customer_id, COUNT(...)) SELECT ... JOIN totals JOIN counts WHERE ...",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
WITH totals AS (
    SELECT customer_id, ROUND(SUM(total_amount), 2) AS total_spent
    FROM orders
    GROUP BY customer_id
),
counts AS (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM orders
    GROUP BY customer_id
)
SELECT c.name AS customer_name, t.total_spent, cnt.order_count
FROM customers c
JOIN totals t   ON c.customer_id = t.customer_id
JOIN counts cnt ON c.customer_id = cnt.customer_id
WHERE t.total_spent > 500
  AND cnt.order_count >= 2
ORDER BY t.total_spent DESC;""",
        "order_matters": False,
        "explanation": (
            "Two CTEs declared in one WITH clause. The commas separate them; "
            "later CTEs can reference earlier ones by name.\n\n"
            "The final SELECT joins both CTEs to the customers table and applies "
            "the combined filter.\n\n"
            "Qualifying customers (total_spent > $500 AND orders >= 2):\n"
            "Alice Chen ($2,049.93, 4), David Kim ($1,695.97, 2), "
            "Emma Rodriguez ($1,409.97, 2), Carol Lee ($781.93, 3), "
            "Bob Martinez ($659.95, 3), Frank Johnson ($649.97, 2).\n\n"
            "Henry Davis ($549.99) and Isabel Wilson ($1,299.99) each have only 1 order — "
            "they pass the spend filter but fail the count filter."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
WITH totals AS (
    SELECT customer_id, ROUND(SUM(total_amount), 2) AS total_spent
    FROM orders GROUP BY customer_id
),
counts AS (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, t.total_spent, cnt.order_count
FROM customers c
JOIN totals t ON c.customer_id = t.customer_id
JOIN counts cnt ON c.customer_id = cnt.customer_id
WHERE t.total_spent > 500 AND cnt.order_count >= 2
ORDER BY t.total_spent DESC;""",
                "correct": True,
                "explanation": "CORRECT. Two CTEs compute spend and count separately; the final SELECT joins and filters on both conditions.",
            },
            {
                "id": "B",
                "text": """\
WITH summary AS (
    SELECT customer_id,
        ROUND(SUM(total_amount), 2) AS total_spent,
        COUNT(order_id) AS order_count
    FROM orders
    GROUP BY customer_id
)
SELECT c.name AS customer_name, s.total_spent, s.order_count
FROM customers c
JOIN summary s ON c.customer_id = s.customer_id
WHERE s.total_spent > 500 AND s.order_count >= 2
ORDER BY s.total_spent DESC;""",
                "correct": True,
                "explanation": "CORRECT (alternative). A single CTE computes both aggregates in one pass — simpler and equally valid when the GROUP BY key is the same.",
            },
            {
                "id": "C",
                "text": """\
WITH totals AS (
    SELECT customer_id, ROUND(SUM(total_amount), 2) AS total_spent
    FROM orders GROUP BY customer_id
),
counts AS (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM totals GROUP BY customer_id
)
SELECT c.name AS customer_name, t.total_spent, cnt.order_count
FROM customers c
JOIN totals t ON c.customer_id = t.customer_id
JOIN counts cnt ON c.customer_id = cnt.customer_id
WHERE t.total_spent > 500 AND cnt.order_count >= 2
ORDER BY t.total_spent DESC;""",
                "correct": False,
                "explanation": "INCORRECT. The counts CTE selects FROM totals instead of FROM orders. Totals has one row per customer (no order_id column), so COUNT(order_id) would always return 0 or error.",
            },
            {
                "id": "D",
                "text": """\
WITH totals AS (
    SELECT customer_id, ROUND(SUM(total_amount), 2) AS total_spent
    FROM orders GROUP BY customer_id
),
counts AS (
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, t.total_spent, cnt.order_count
FROM customers c
JOIN totals t ON c.customer_id = t.customer_id
JOIN counts cnt ON c.customer_id = cnt.customer_id
HAVING t.total_spent > 500 AND cnt.order_count >= 2
ORDER BY t.total_spent DESC;""",
                "correct": False,
                "explanation": "INCORRECT. HAVING without GROUP BY applies to the entire result as a single group — it returns either all rows or none, not filtered rows per customer.",
            },
        ],
    },

    # ── 20 ───────────────────────────────────────────────────
    {
        "id": 20,
        "title": "Combining Result Sets with UNION ALL",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "UNION stacks the results of two or more SELECT statements vertically. "
            "Both queries must return the same number of columns with compatible types. "
            "UNION removes duplicates; UNION ALL keeps all rows (faster when duplicates "
            "are impossible or don't matter)."
        ),
        "question": (
            "Write a query that lists all customers who have placed no orders alongside "
            "all departments that have no employees. Use two separate SELECT statements "
            "combined with UNION ALL. Each row should have two columns: entity_name and entity_type "
            "(e.g., 'No-order customer' or 'Empty department'). Order by entity_type, then entity_name."
        ),
        "hint": "SELECT name, 'No-order customer' FROM customers WHERE ... UNION ALL SELECT department_name, 'Empty department' FROM departments WHERE ...",
        "tables": [CUSTOMERS, ORDERS, DEPARTMENTS, EMPLOYEES],
        "correct_query": """\
SELECT c.name AS entity_name, 'No-order customer' AS entity_type
FROM customers c
WHERE c.customer_id NOT IN (SELECT customer_id FROM orders)
UNION ALL
SELECT d.department_name, 'Empty department'
FROM departments d
WHERE d.department_id NOT IN (SELECT department_id FROM employees)
ORDER BY entity_type, entity_name;""",
        "order_matters": False,
        "explanation": (
            "**UNION ALL** stacks the two result sets without deduplication. "
            "Since the two sets can never share the same entity_name + entity_type combination, "
            "UNION and UNION ALL produce identical results here — but UNION ALL is preferred "
            "when no deduplication is needed because it avoids the sorting cost.\n\n"
            "Result set 1: Oliver White, Sophia Harris (customers with no orders)\n"
            "Result set 2: HR (department with no employees)\n\n"
            "3 rows total."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT c.name AS entity_name, 'No-order customer' AS entity_type
FROM customers c
WHERE c.customer_id NOT IN (SELECT customer_id FROM orders)
UNION ALL
SELECT d.department_name, 'Empty department'
FROM departments d
WHERE d.department_id NOT IN (SELECT department_id FROM employees)
ORDER BY entity_type, entity_name;""",
                "correct": True,
                "explanation": "CORRECT. UNION ALL combines the two unrelated result sets; ORDER BY applies to the final combined output.",
            },
            {
                "id": "B",
                "text": """\
SELECT c.name AS entity_name, 'No-order customer' AS entity_type
FROM customers c
WHERE c.customer_id NOT IN (SELECT customer_id FROM orders)
UNION ALL
SELECT d.department_name, 'Empty department', d.location
FROM departments d
WHERE d.department_id NOT IN (SELECT department_id FROM employees)
ORDER BY entity_type, entity_name;""",
                "correct": False,
                "explanation": "INCORRECT. The second SELECT has 3 columns but the first has 2 — UNION ALL requires both queries to return the same number of columns.",
            },
            {
                "id": "C",
                "text": """\
SELECT c.name AS entity_name, 'No-order customer' AS entity_type
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
INTERSECT
SELECT d.department_name, 'Empty department'
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.employee_id IS NULL
ORDER BY entity_type, entity_name;""",
                "correct": False,
                "explanation": "INCORRECT. INTERSECT returns only rows that appear in BOTH result sets — since no customer name matches a department name, this returns zero rows.",
            },
            {
                "id": "D",
                "text": """\
SELECT c.name AS entity_name, 'No-order customer' AS entity_type
FROM customers c
WHERE c.customer_id NOT IN (SELECT customer_id FROM orders)
UNION
SELECT d.department_name, 'Empty department'
FROM departments d
WHERE d.department_id NOT IN (SELECT department_id FROM employees)
ORDER BY entity_type, entity_name;""",
                "correct": True,
                "explanation": "CORRECT (alternative). UNION also works here because there are no duplicate rows across the two sets. UNION ALL (choice A) is preferred for performance.",
            },
        ],
    },

    # ── 21 ───────────────────────────────────────────────────
    {
        "id": 21,
        "title": "Monthly Revenue Summary for Q1 2024",
        "difficulty": "Medium",
        "category": "Aggregation & Grouping",
        "description": (
            "Filtering and aggregating on date ranges is a common reporting pattern. "
            "EXTRACT() pulls a specific date part (year, month, day) as a number, "
            "which you can then GROUP BY for time-series summaries."
        ),
        "question": (
            "Write a query summarising orders placed in Q1 2024 (January through March). "
            "Show the month number (aliased month), order count (aliased order_count), "
            "and total revenue (aliased monthly_revenue, rounded to 2 decimals). "
            "Order by month ascending."
        ),
        "hint": "WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31' then GROUP BY EXTRACT(MONTH FROM order_date).",
        "tables": [ORDERS],
        "correct_query": """\
SELECT
    EXTRACT(MONTH FROM order_date)::INTEGER AS month,
    COUNT(order_id)                          AS order_count,
    ROUND(SUM(total_amount), 2)              AS monthly_revenue
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month;""",
        "order_matters": True,
        "explanation": (
            "**EXTRACT(MONTH FROM order_date)** returns the month number (1–12). "
            "Casting to INTEGER (::INTEGER) is optional but keeps the output clean.\n\n"
            "**WHERE order_date BETWEEN** filters rows before grouping — "
            "the date range is inclusive on both ends.\n\n"
            "Q1 2024 results:\n"
            "- January (orders 1,2,3): 3 orders, $1,839.94\n"
            "- February (orders 4,5,6): 3 orders, $2,249.97\n"
            "- March (orders 7,8,9,10): 4 orders, $851.90"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT EXTRACT(MONTH FROM order_date)::INTEGER AS month,
    COUNT(order_id) AS order_count,
    ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month;""",
                "correct": True,
                "explanation": "CORRECT. EXTRACT(MONTH) groups by month number; WHERE filters to Q1 2024 before aggregation.",
            },
            {
                "id": "B",
                "text": """\
SELECT DATE_TRUNC('month', order_date) AS month,
    COUNT(order_id) AS order_count,
    ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;""",
                "correct": False,
                "explanation": "INCORRECT (for this question). DATE_TRUNC returns the first day of the month (e.g., 2024-01-01) rather than the month number. The output format does not match the asked alias 'month' as a number.",
            },
            {
                "id": "C",
                "text": """\
SELECT EXTRACT(MONTH FROM order_date)::INTEGER AS month,
    COUNT(order_id) AS order_count,
    ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024
    AND EXTRACT(MONTH FROM order_date) BETWEEN 1 AND 3
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Using EXTRACT for year and month filtering instead of BETWEEN on the date achieves the same Q1 2024 filter.",
            },
            {
                "id": "D",
                "text": """\
SELECT EXTRACT(MONTH FROM order_date)::INTEGER AS month,
    COUNT(order_id) AS order_count,
    ROUND(SUM(total_amount), 2) AS monthly_revenue
FROM orders
GROUP BY EXTRACT(MONTH FROM order_date)
HAVING EXTRACT(YEAR FROM order_date) = 2024
    AND EXTRACT(MONTH FROM order_date) BETWEEN 1 AND 3
ORDER BY month;""",
                "correct": False,
                "explanation": "INCORRECT. HAVING filters after grouping; non-aggregate expressions in HAVING are valid but semantically confusing here. Worse, the GROUP BY includes all years, so the months 1–3 across 2023 and 2024 are merged into the same groups before the HAVING filter.",
            },
        ],
    },

    # ── 22 ───────────────────────────────────────────────────
    {
        "id": 22,
        "title": "Top 5 Products by Revenue",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "Ranking products by revenue requires joining line-item data to the product "
            "catalogue and aggregating across multiple orders. LIMIT is the "
            "straightforward way to cap the result set to the top-N rows."
        ),
        "question": (
            "Using the order_items and products tables, write a query showing the top 5 "
            "products by total revenue (quantity × unit_price). Include product name, "
            "category, total units sold (aliased total_units_sold), and total revenue "
            "(aliased total_revenue, rounded to 2 decimals). Order by total_revenue descending."
        ),
        "hint": "JOIN order_items to products, SUM(quantity * unit_price) GROUP BY product, ORDER BY total_revenue DESC LIMIT 5.",
        "tables": [ORDER_ITEMS, PRODUCTS],
        "correct_query": """\
SELECT
    p.name AS product_name,
    p.category,
    SUM(oi.quantity)                          AS total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC
LIMIT 5;""",
        "order_matters": True,
        "explanation": (
            "**JOIN order_items to products** links each line item to its product metadata.\n\n"
            "**SUM(quantity * unit_price)** computes actual revenue, accounting for quantities > 1.\n\n"
            "**GROUP BY p.product_id, p.name, p.category** — including product_id prevents "
            "two products with the same name from being merged, and satisfies the GROUP BY "
            "requirement for all non-aggregated columns.\n\n"
            "Top 5:\n"
            "1. Laptop Pro (Electronics) — 4 units, $5,199.96\n"
            "2. Standing Desk (Furniture) — 2 units, $1,099.98\n"
            "3. Monitor 27in (Electronics) — 3 units, $1,049.97\n"
            "4. Office Chair (Furniture) — 2 units, $799.98\n"
            "5. Headphones (Electronics) — 4 units, $599.96"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT p.name AS product_name, p.category,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC
LIMIT 5;""",
                "correct": True,
                "explanation": "CORRECT. Joins, groups by product, aggregates quantity and revenue, orders desc, limits to 5.",
            },
            {
                "id": "B",
                "text": """\
SELECT p.name AS product_name, p.category,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_units_sold DESC
LIMIT 5;""",
                "correct": False,
                "explanation": "INCORRECT. Orders by total_units_sold instead of total_revenue — Pen Pack (5 units × $8.99 = $44.95) would appear instead of Office Chair (2 units × $399.99 = $799.98).",
            },
            {
                "id": "C",
                "text": """\
SELECT p.name AS product_name, p.category,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * p.price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC
LIMIT 5;""",
                "correct": False,
                "explanation": "INCORRECT. Uses p.price (list price from the products table) instead of oi.unit_price (actual price at time of order). These can differ due to discounts or price changes.",
            },
            {
                "id": "D",
                "text": """\
SELECT p.name AS product_name, p.category,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
ORDER BY total_revenue DESC
LIMIT 5;""",
                "correct": False,
                "explanation": "INCORRECT. Missing GROUP BY — without it, aggregate functions apply to the entire joined table and the query returns only one row (or raises an error depending on the database).",
            },
        ],
    },

    # ── 23 ───────────────────────────────────────────────────
    {
        "id": 23,
        "title": "ROW_NUMBER vs RANK vs DENSE_RANK",
        "difficulty": "Medium",
        "category": "Window Functions",
        "description": (
            "Three ranking functions look similar but behave differently around ties. "
            "ROW_NUMBER always assigns unique sequential integers. RANK skips numbers after "
            "a tie. DENSE_RANK never skips — the next distinct value always gets the next integer."
        ),
        "question": (
            "Write a query showing every employee's name, salary, and all three ranking functions "
            "applied globally (not per department): row_num (ROW_NUMBER), rank_val (RANK), "
            "and dense_rank_val (DENSE_RANK). All ordered by salary descending. "
            "Use name as a secondary sort for ROW_NUMBER to make it deterministic. "
            "Order the results by salary descending, then name."
        ),
        "hint": "Three separate OVER clauses: ROW_NUMBER() OVER (ORDER BY salary DESC, name), RANK() OVER (ORDER BY salary DESC), DENSE_RANK() OVER (ORDER BY salary DESC)",
        "tables": [EMPLOYEES],
        "correct_query": """\
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC, name)  AS row_num,
    RANK()       OVER (ORDER BY salary DESC)         AS rank_val,
    DENSE_RANK() OVER (ORDER BY salary DESC)         AS dense_rank_val
FROM employees
ORDER BY salary DESC, name;""",
        "order_matters": False,
        "explanation": (
            "With the employees dataset (10 rows, several salary ties):\n\n"
            "David Brown & Frank Miller both earn $110k:\n"
            "- ROW_NUMBER: 1 and 2 (unique, tiebreak by name: David < Frank)\n"
            "- RANK: both get 1, next person (Emma) gets 3\n"
            "- DENSE_RANK: both get 1, Emma gets 2\n\n"
            "Alice Johnson & Carol Williams both earn $95k:\n"
            "- ROW_NUMBER: 4 and 5\n"
            "- RANK: both get 4; next (Bob) gets 6\n"
            "- DENSE_RANK: both get 3; Bob gets 4\n\n"
            "Choose ROW_NUMBER when you need exactly one row per rank (e.g., top-N). "
            "Choose DENSE_RANK when you don't want gaps in rank numbers."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC, name) AS row_num,
    RANK()       OVER (ORDER BY salary DESC)        AS rank_val,
    DENSE_RANK() OVER (ORDER BY salary DESC)        AS dense_rank_val
FROM employees
ORDER BY salary DESC, name;""",
                "correct": True,
                "explanation": "CORRECT. Three separate window functions with appropriate ORDER BY clauses. ROW_NUMBER has a name tiebreaker for determinism.",
            },
            {
                "id": "B",
                "text": """\
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank_val,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS dense_rank_val
FROM employees
ORDER BY salary DESC, name;""",
                "correct": False,
                "explanation": "INCORRECT. All three columns use ROW_NUMBER — they produce identical values and do not demonstrate the difference between the ranking functions.",
            },
            {
                "id": "C",
                "text": """\
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC, name) AS row_num,
    RANK()       OVER (ORDER BY salary DESC)        AS rank_val,
    DENSE_RANK() OVER (ORDER BY salary DESC)        AS dense_rank_val
FROM employees
ORDER BY row_num;""",
                "correct": False,
                "explanation": "INCORRECT. ORDER BY row_num (always unique 1–10) produces the same order as salary DESC — but obscures the relationship since row_num is determined by the window, not the final sort.",
            },
            {
                "id": "D",
                "text": """\
SELECT name, salary,
    ROW_NUMBER() OVER (PARTITION BY salary ORDER BY name) AS row_num,
    RANK()       OVER (ORDER BY salary DESC)               AS rank_val,
    DENSE_RANK() OVER (ORDER BY salary DESC)               AS dense_rank_val
FROM employees
ORDER BY salary DESC, name;""",
                "correct": False,
                "explanation": "INCORRECT. ROW_NUMBER uses PARTITION BY salary which resets numbering within each salary group — row_num no longer represents a global rank, breaking the comparison intent.",
            },
        ],
    },

    # ── 24 ───────────────────────────────────────────────────
    {
        "id": 24,
        "title": "Inactive Customers Using CTEs and Date Arithmetic",
        "difficulty": "Medium",
        "category": "CTEs (Common Table Expressions)",
        "description": (
            "Date arithmetic is common in CRM and retention analysis. "
            "Here you'll combine two CTEs — one to find each customer's most recent order date, "
            "one to compute the cutoff — to flag customers who haven't ordered recently."
        ),
        "question": (
            "Define 'inactive' as: the customer's most recent order was more than 60 days "
            "before the latest order date in the entire dataset. "
            "Write a query (using CTEs) returning inactive customers' names and their "
            "last_order_date, ordered from oldest last order to most recent."
        ),
        "hint": "CTE 1: MAX(order_date) - INTERVAL '60 days' as cutoff. CTE 2: MAX(order_date) per customer. Then join and filter WHERE last_order_date < cutoff.",
        "tables": [CUSTOMERS, ORDERS],
        "correct_query": """\
WITH cutoff AS (
    SELECT MAX(order_date) - INTERVAL '60 days' AS cutoff_date
    FROM orders
),
last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders
    GROUP BY customer_id
)
SELECT c.name AS customer_name, lo.last_order_date
FROM customers c
JOIN last_orders lo ON c.customer_id = lo.customer_id
CROSS JOIN cutoff
WHERE lo.last_order_date < cutoff.cutoff_date
ORDER BY lo.last_order_date;""",
        "order_matters": False,
        "explanation": (
            "The latest order in the dataset is 2024-06-10. "
            "60 days earlier = 2024-04-11 (the cutoff).\n\n"
            "Customers with last order before 2024-04-11:\n"
            "- Grace Brown: last order 2024-04-01\n"
            "- Bob Martinez: last order 2024-04-10\n\n"
            "**INTERVAL '60 days'** is standard PostgreSQL/DuckDB date arithmetic. "
            "The cutoff CTE returns a single row, so CROSS JOIN merges it with every "
            "customer row without increasing the row count.\n\n"
            "Alternative: pass cutoff as a scalar subquery in WHERE:\n"
            "WHERE lo.last_order_date < (SELECT MAX(order_date) - INTERVAL '60 days' FROM orders)"
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
WITH cutoff AS (
    SELECT MAX(order_date) - INTERVAL '60 days' AS cutoff_date FROM orders
),
last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, lo.last_order_date
FROM customers c
JOIN last_orders lo ON c.customer_id = lo.customer_id
CROSS JOIN cutoff
WHERE lo.last_order_date < cutoff.cutoff_date
ORDER BY lo.last_order_date;""",
                "correct": True,
                "explanation": "CORRECT. Two CTEs compute the cutoff date and per-customer last order; CROSS JOIN adds the single cutoff row to each customer row for comparison.",
            },
            {
                "id": "B",
                "text": """\
WITH cutoff AS (
    SELECT MAX(order_date) - 60 AS cutoff_date FROM orders
),
last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, lo.last_order_date
FROM customers c
JOIN last_orders lo ON c.customer_id = lo.customer_id
CROSS JOIN cutoff
WHERE lo.last_order_date < cutoff.cutoff_date
ORDER BY lo.last_order_date;""",
                "correct": False,
                "explanation": "INCORRECT. Subtracting an integer from a DATE (MAX(order_date) - 60) is not standard SQL. In PostgreSQL/DuckDB use INTERVAL '60 days' for date arithmetic.",
            },
            {
                "id": "C",
                "text": """\
WITH last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, lo.last_order_date
FROM customers c
JOIN last_orders lo ON c.customer_id = lo.customer_id
WHERE lo.last_order_date < (
    SELECT MAX(order_date) - INTERVAL '60 days' FROM orders
)
ORDER BY lo.last_order_date;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Uses a scalar subquery in WHERE instead of a second CTE — simpler and equally valid.",
            },
            {
                "id": "D",
                "text": """\
WITH cutoff AS (
    SELECT MAX(order_date) - INTERVAL '60 days' AS cutoff_date FROM orders
),
last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders GROUP BY customer_id
)
SELECT c.name AS customer_name, lo.last_order_date
FROM customers c
JOIN last_orders lo ON c.customer_id = lo.customer_id
JOIN cutoff ON lo.last_order_date < cutoff.cutoff_date
ORDER BY lo.last_order_date;""",
                "correct": True,
                "explanation": "CORRECT (alternative). Using JOIN cutoff ON ... < cutoff_date as the join condition is equivalent to CROSS JOIN + WHERE and produces the same result.",
            },
        ],
    },

    # ── 25 ───────────────────────────────────────────────────
    {
        "id": 25,
        "title": "All Products with Revenue Using COALESCE",
        "difficulty": "Medium",
        "category": "Joins",
        "description": (
            "When you LEFT JOIN a fact table onto a dimension table, "
            "products with no sales have NULL in every aggregated column. "
            "COALESCE(expression, fallback) replaces NULL with a default value — "
            "essential for clean reporting."
        ),
        "question": (
            "Using the products and order_items tables (which includes two unsold products: "
            "Whiteboard and Ergonomic Mat), write a query returning every product's name, "
            "category, total units sold (aliased units_sold), and total revenue "
            "(aliased total_revenue, rounded to 2 decimals). "
            "Unsold products should show 0 for both columns, not NULL. "
            "Order by total_revenue descending, then product name."
        ),
        "hint": "LEFT JOIN from products to order_items. COALESCE(SUM(quantity), 0) and COALESCE(ROUND(SUM(quantity * unit_price), 2), 0) handle the NULL case.",
        "tables": [PRODUCTS_EXTENDED, ORDER_ITEMS],
        "correct_query": """\
SELECT
    p.name AS product_name,
    p.category,
    COALESCE(SUM(oi.quantity), 0)                          AS units_sold,
    COALESCE(ROUND(SUM(oi.quantity * oi.unit_price), 2), 0) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC, p.name;""",
        "order_matters": False,
        "explanation": (
            "**LEFT JOIN** from products (left) to order_items (right) keeps all product rows. "
            "For Whiteboard (product 13) and Ergonomic Mat (product 14), no order_items rows "
            "exist, so all order_items columns come back as NULL.\n\n"
            "**SUM(NULL values)** returns NULL, not 0. "
            "**COALESCE(SUM(...), 0)** substitutes 0 when SUM returns NULL.\n\n"
            "**INNER JOIN** would silently omit unsold products — always ask: "
            "'should missing data appear as zero or be excluded?' "
            "before choosing the join type."
        ),
        "choices": [
            {
                "id": "A",
                "text": """\
SELECT p.name AS product_name, p.category,
    COALESCE(SUM(oi.quantity), 0) AS units_sold,
    COALESCE(ROUND(SUM(oi.quantity * oi.unit_price), 2), 0) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC, p.name;""",
                "correct": True,
                "explanation": "CORRECT. LEFT JOIN retains unsold products; COALESCE converts NULL aggregates to 0.",
            },
            {
                "id": "B",
                "text": """\
SELECT p.name AS product_name, p.category,
    COALESCE(SUM(oi.quantity), 0) AS units_sold,
    COALESCE(ROUND(SUM(oi.quantity * oi.unit_price), 2), 0) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC, p.name;""",
                "correct": False,
                "explanation": "INCORRECT. INNER JOIN (JOIN) discards products with no matching order_items rows — Whiteboard and Ergonomic Mat disappear from the result entirely, making COALESCE irrelevant.",
            },
            {
                "id": "C",
                "text": """\
SELECT p.name AS product_name, p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC, p.name;""",
                "correct": False,
                "explanation": "INCORRECT. Missing COALESCE — unsold products display NULL for units_sold and total_revenue instead of 0. The problem explicitly requires 0.",
            },
            {
                "id": "D",
                "text": """\
SELECT p.name AS product_name, p.category,
    COALESCE(SUM(oi.quantity), 0) AS units_sold,
    COALESCE(ROUND(SUM(oi.quantity * oi.unit_price), 2), 0) AS total_revenue
FROM order_items oi
LEFT JOIN products p ON p.product_id = oi.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_revenue DESC, p.name;""",
                "correct": False,
                "explanation": "INCORRECT. The LEFT JOIN is reversed — order_items is the left (driving) table, so only products that have been ordered appear. Unsold products are excluded.",
            },
        ],
    },

]
