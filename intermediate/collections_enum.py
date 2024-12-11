from collections import defaultdict


def count_products(orders: list[str]) -> defaultdict:
    product_count = defaultdict(int)
    for order in orders:
        product_count[order] += 1
    return product_count


orders = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = count_products(orders)
print(count)
