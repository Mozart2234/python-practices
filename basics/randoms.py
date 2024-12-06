import random

# generate a random number
rand_num = random.randint(0, 100)
print(rand_num)

# generate a random color
colors = ["red", "blue", "green"]
rand_color = random.choice(colors)
print(rand_color)

# Suffle a card list
cards = ["Ace", "King", "Queen", "Jack"]
print(cards)
random.shuffle(cards)
print(cards)
