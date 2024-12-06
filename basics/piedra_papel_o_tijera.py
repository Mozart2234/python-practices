from random import randint

print("Piedra papel o tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

player_choice = int(input("Elije una opción: "))

cpu_choice = randint(1, 3)

if player_choice and cpu_choice:
    print("Empate")
elif (
    (player_choice == 1 and cpu_choice == 3)
    or (player_choice == 2 and cpu_choice == 1)
    or (player_choice == 3 and cpu_choice == 2)
):
    print("Ganaste")
else:
    print("Perdiste")
