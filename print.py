# basic print statement
print("Hello, World!")

# print using a comma
print("Hello", "World!")

#using sep
print("Hello", "World!", sep=",")

#using end
print("Hello", end=" ")
print("World!")

#using variables
name = "John"
last_name = "Doe"
print("Name", name, "Last Name", last_name)

#using f-string
print(f"Name {name} Last Name {last_name}")

#using format
print("Name {} Last Name {}".format(name, last_name))

#using format in numbers
float_number = 5.678123
print("Float number: {:.2f}".format(float_number))

#print escape characters
print("Hello\nWorld!")
print("Hello world!, my name is 'John Doe'")
