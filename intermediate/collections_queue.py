from collections import deque


def manage_delivery_queue() -> deque:
    delivery_queue = deque(["apple", "banana", "orange"])
    delivery_queue.append("mango")
    delivery_queue.append("grapes")
    delivery_queue.appendleft("kiwi")
    delivery_queue.pop()

    return delivery_queue


print(manage_delivery_queue())
