def greet(name, last_name="Sin apellido"):
    print("Hello,", name, last_name)


greet("Alexei", "Mamani")
greet("Tefi")
greet(last_name="Mamani", name="Jean Paul")

print("-" * 50)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    while True:
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = int(input("Opción: "))

        if option == 5:
            print("Hasta luego!")
            break

        if option < 1 or option > 5:
            print("Opción inválida")
            continue

        if option in [1, 2, 3, 4]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if option == 1:
                print("Resultado:", add(a, b))
            elif option == 2:
                print("Resultado:", subtract(a, b))
            elif option == 3:
                print("Resultado:", multiply(a, b))
            elif option == 4:
                print("Resultado:", divide(a, b))


calculator()
