x = "global"


def outer_function():
    x = "outer"

    def inner_function():
        x = "inner"
        print(x)

    inner_function()
    print(x)


outer_function()
print(x)
