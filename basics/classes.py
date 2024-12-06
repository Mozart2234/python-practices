class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def greet(self):
        return f"Hello, my name is {self.name}"


alexei = Person("Alexei", 25)
print(alexei)
print(alexei.greet())

tefi = Person("Tefi", 24)
print(tefi)
print(tefi.greet())
