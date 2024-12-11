def sum_numbers(*args):
    print(args)
    return sum(args)


def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print(sum_numbers(1, 2, 3, 4, 5))
    print(print_info(name="John", age=30, city="New York"))
