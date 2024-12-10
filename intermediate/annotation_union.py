from typing import Union


def process_salary(salary: Union[int, float]) -> str:
    """
    Process the salary of an employee.

    Parameters:
    salary (Union[int, float]): Salary of an employee.

    Returns:
    str: Processed salary of an employee.
    """
    return f"Salary: {salary}"


print(process_salary(50000))
print(process_salary(50000.0))
