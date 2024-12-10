from typing import Optional


def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Find the index of the employee ID in the list of employee IDs.

    Parameters:
    employee_ids (list[int]): List of employee IDs.
    employee_id (int): Employee ID to find.

    Returns:
    Optional[int]: Index of the employee ID in the list of employee IDs.
    """
    if employee_id:
        return employee_ids.index(employee_id)
    return None
