def my_generator():
    yield 1
    yield 2
    yield 3


for i in my_generator():
    print(i)

print("")


def fibbonaci_generator(limit):
    x, y = 0, 1
    if limit < 1:
        return None

    while x < limit:
        yield x
        x, y = y, x + y


for i in fibbonaci_generator(100):
    print(i)

print("")


def odd_generator(limit):
    for i in range(limit + 1):
        if i % 2 != 0:
            yield i


print("")
for i in odd_generator(10):
    print(i)

print("")


def even_generator(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i


for i in even_generator(10):
    print(i)
