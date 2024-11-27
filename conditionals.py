x = 11
y = 20

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor a 5")

print("-" * 20)
print("Fuera del condicional", end="\n\n")

if x > 10 and y > 25:
    print("x es mayor que 10 y y es mayor que 25")

if x > 10 or y > 25:
    print("x es mayor que 10 o y es mayor que 25")

if not x > 10:
    print("x no es mayor que 10")
