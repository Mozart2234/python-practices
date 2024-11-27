add = lambda a, b: a + b
print(add(1, 2))

multiply = lambda a, b: a * b
print(multiply(2, 3))

# squares of numbers
numbers = range(11)

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# even numbers

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
