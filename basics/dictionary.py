numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

print(numbers)
print(type(numbers))

print(numbers[2])

info = {
        'name': 'Alexei',
        'lastname': 'Mamani',
        'age': 30,
}


print(info)
del info['age']
print(info)
print(info['name'])

keys = info.keys()
print(keys)

values = info.values()
print(values)

items = info.items()
print(items)

contacts = {
        'friends': ['Alexei', 'Juan', 'Pedro'],
        'family': ['Mamani', 'Perez', 'Gomez']
        }

print(contacts)
print("Friends: ", contacts['friends'])
print("Family: ", contacts['family'])


