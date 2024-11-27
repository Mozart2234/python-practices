is_member = True
age = 15

if is_member:
    if age < 18:
        print("Eres miembro y eres menor de edad, no puedes entrar")
    elif age >= 18:
        print("Eres miembro y eres mayor de edad, puedes entrar")
else:
    print("No eres miembro, no puedes entrar")
