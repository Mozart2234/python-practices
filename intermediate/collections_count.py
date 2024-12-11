from collections import Counter


def count_sales(sales: list[str]) -> Counter:
    return Counter(sales)


sales = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = count_sales(sales)
print(result)
