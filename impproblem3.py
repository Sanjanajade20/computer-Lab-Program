# Sample data: a list of dictionaries for employees
employees = [
    {"dept_no": "D01", "roll_no": "E101", "salary": 50000},
    {"dept_no": "D01", "roll_no": "E102", "salary": 60000},
    {"dept_no": "D02", "roll_no": "E201", "salary": 55000},
    {"dept_no": "D02", "roll_no": "E202", "salary": 45000},
    {"dept_no": "D03", "roll_no": "E301", "salary": 70000},
    {"dept_no": "D03", "roll_no": "E302", "salary": 65000},
]

dept_salaries = {}

for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

for dept, salaries in dept_salaries.items():
    print(f"Department {dept}:")
    print(f"  Min Salary: {min(salaries)}")
    print(f"  Max Salary: {max(salaries)}")
