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

Run steps 0, 1 and 2 to reset:
Run Steps 3 and 4 to execute app function:

Step 0 - Web Address to app.py website: http://127.0.0.1:5000
Get ollama+qwen2-7b JSON output or Error Message: http://127.0.0.1:5000/api/test_ollama

Step 1 - Kill every running Python process:
Get-Process -Name python -ErrorAction SilentlyContinue | Stop-Process -Force

Step 2 - Verify port 5000 is free:
netstat -ano | findstr ":5000"
This should return nothing. If it still shows something, note the PID (last column) and run:
taskkill /PID <that_PID> /F



Step 3 - Start fresh from the correct folder:
cd "c:\Users\matth\Documents\Claude_Code_Textbooks\Static SQL Practice"
python app.py

Step 4 - Look at the terminal output. You should see something like:
[app.py] Loading from: C:\Users\matth\Documents\...\app.py
[app.py] Routes registered: ['/', '/api/bank_problem', '/api/test_ollama', '/api/problem', '/api/submit', ...]
 * Running on http://127.0.0.1:5000

If /api/test_ollama appears in that routes list, the new code is running. If you instead see an error like Address already in use or OSError, share it here and we'll fix it. If the routes list is missing test_ollama, share the full output so I can see what's actually loading.



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
