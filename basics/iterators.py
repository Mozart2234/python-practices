my_list = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print("")

text = "Hello World"
iter_text = iter(text)

for char in iter_text:
    print(char)

print("")

limit = 10

odd_iter = iter(range(1, limit + 1, 2))
for num in odd_iter:
    print(num)

print("")

even_iter = iter(range(0, limit + 1, 2))
for num in even_iter:
    print(num)
