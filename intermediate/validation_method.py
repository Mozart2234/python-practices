def divide(a: int, b: int) -> float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")

    if b == 0:
        raise ValueError("b must not be zero")

    return a / b


print(divide(10, 2))

try:
    print(divide(10, "2"))
except (ValueError, TypeError) as e:
    print("Error:", e)
