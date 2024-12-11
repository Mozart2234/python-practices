def check_access(role):
    def decorator(func):
        def wrapper(employee):
            if employee.get("role") == role:
                return func(employee)
            else:
                print(
                    "ACCESS DENIED: You don't have permission to access this resource"
                )

        return wrapper

    return decorator


def log_action(func):
    def wrapper(employee):
        print(f"Performing action: {func.__name__}")
        return func(employee)

    return wrapper


@check_access("admin")
@log_action
def delete_employee(employee):
    print(f'Deleting employee {employee.get("name")}')


employee = {"name": "Jane Doe", "role": "employee"}
admin = {"name": "John Doe", "role": "admin"}

delete_employee(admin)
delete_employee(employee)
