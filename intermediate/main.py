def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


if __name__ == "__main__":
    print("Math operations")
    print("1 + 2 =", add(1, 2))
    print("3 - 4 =", subtract(3, 4))
    print("5 * 6 =", multiply(5, 6))
    print("8 / 2 =", divide(8, 2))
