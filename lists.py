todo_list = ["Go to the market", "Buy a new phone", "Read a book"]
print(todo_list, type(todo_list))
print("Length fo todo_list:" ,len(todo_list))

todo_list_numbers = [1, 2, 3, 4, 5]
print(todo_list_numbers, type(todo_list_numbers))

todo_list_combined = ["Go to the market", 1, "Buy a new phone", 2, "Read a book", 3]
print(todo_list_combined, type(todo_list_combined))

print(todo_list[0])
print(todo_list[1])
print(todo_list[-1])

string = "Hello World"
print(string, type(string))
print(string[0])
print(string[1])

# Slicing
print(todo_list[0:2])
print(todo_list[:2])
print(todo_list[1:])

# Concatenation
print(todo_list_combined)
todo_list_combined.append("Learn Python")
todo_list_combined.append(True)
print(todo_list_combined)

# Insert
print(todo_list_combined)
todo_list_combined.insert(1, "Hello")
print(todo_list_combined)
print(todo_list_combined.index("Hello"))

# Min and Max
print("Max", min(todo_list_numbers))
print("Mix", max(todo_list_numbers))

# Delete
del todo_list_combined[-1]
print(todo_list_combined)

del todo_list_combined[:2]
print(todo_list_combined)

del todo_list_combined
print(todo_list_combined)



