import multiprocessing


def calculate_square(number):
    return number * number


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print("Results", results)
