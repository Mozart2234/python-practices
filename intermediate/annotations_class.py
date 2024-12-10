class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I earn {self.salary}."


emp = Employee("John", 25, 50000.0)
print(emp.introduce())
