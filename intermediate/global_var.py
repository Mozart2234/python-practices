x = 5


def modify_global():
    global x
    x = 10
    print(x)


modify_global()
print(x)
