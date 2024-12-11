def check_access(func):
    def wrapper(employee):
        if employee.get("role") == "admin":
            return func(employee)
        else:
            print("ACCESS DENIED: You don't have permission to access this resource")

    return wrapper


@check_access
def delete_employee(employee):
    print(f'Deleting employee {employee.get("name")}')


admin = {"name": "John Doe", "role": "admin"}
employee = {"name": "Jane Doe", "role": "employee"}

delete_employee(admin)
delete_employee(employee)
