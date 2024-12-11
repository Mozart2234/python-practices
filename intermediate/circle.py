class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius**2

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")

        self._radius = value


circle = Circle(2)
print(circle.area)
print(circle.radius)

circle.radius = 3
print(circle.area)
print(circle.radius)
