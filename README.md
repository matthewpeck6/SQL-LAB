# SQL-LAB
A program to practice SQL questions focused on more difficult problems like Window Functions, CTEs (Common Table Expressions), Subqueries, and Joins

SQL Practice Lab —- Complete
Files created:

app.py - Flask server
database.py - DuckDB execution + grading engine
problems.py - 10 problems with full datasets
templates/index.html - UI
static/style.css - Dark theme
static/script.js - Frontend logic
requirements.txt


Run Steps 1 and 2 to run the weblink app

Step 1 - Start fresh from the correct folder:
cd into the directory with the repository and run the following command:
python app.py

Step 2 - Look at the terminal output. You should see something like:
[app.py] Loading from: C:/.../SQL-LAB/app.py
[app.py] Routes registered: ['/', '/api/bank_problem', '/api/test_ollama', '/api/problem', '/api/submit', ...]
 * Running on web_link


Total: 65 questions
Easy:   15
Medium: 35
Hard:   15

Topics List: 
Window Functions
CTEs (Common Table Expressions)
Subqueries
Joins
Grouping
Aggregation
Filtering & Sorting
Recursive CTEs

Count  Category                           Difficulty Mix
(19)   Window Functions                   5M(problems.py) + 2H(problems.py) + 6M(qb_m1) + 2M(qb_m2) + 4H(qb_hard)
(15)   Joins                              7M(problems.py) + 1H(problems.py) + 3E(qb_easy) + 2M(qb_m1) + 1M(qb_m2) + 1H(qb_hard)
(12)   Aggregation & Grouping             3M(problems.py) + 6E(qb_easy) + 1M(qb_m1) + 2M(qb_m2)
( 7)   CTEs (Common Table Expressions)    2M(problems.py) + 1H(problems.py) + 1M(qb_m1) + 3H(qb_hard)
( 6)   Filtering & Sorting                6E(qb_easy)
( 5)   Subqueries                         3M(problems.py) + 1H(problems.py) + 1H(qb_hard)
( 1)   Recursive CTEs                     1H(qb_hard)

Next Steps to improve Notable gaps if you want better coverage:
Filtering & Sorting - 6 questions,  all Easy,  all in qb_easy,  zero Medium/Hard
Recursive CTEs - only 1 question total
Subqueries - only 5 questions,  nothing Easy
