from typing import Optional


def order_employees(
    employees: list[dict], salary_amount: float
) -> Optional[list[dict]]:
    return [employee for employee in employees if employee["salary"] > salary_amount]


employees = [
    {"name": "John", "age": 25, "salary": 50000.0},
    {"name": "Jane", "age": 30, "salary": 60000.0},
    {"name": "Doe", "age": 35, "salary": 70000.0},
    {"name": "Smith", "age": 40, "salary": 80000.0},
]

print(order_employees(employees, 60000.0))
