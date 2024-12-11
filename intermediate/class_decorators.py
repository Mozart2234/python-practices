class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


print(Calculator.add(1, 2))


class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
