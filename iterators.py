numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print("Number:", i)

print("")
for i in range(3, 10):
    print("Number using range:", i)

fruits = ["apple", "banana", "cherry", "elderberry", "fig", "grape"]

for fruit in fruits:
    print("Fruit:", fruit)
    if fruit == "cherry":
        print("Found cherry!!!")
        break

print("")

x = 0
while x < 5:
    print("X:", x)
    x += 1
