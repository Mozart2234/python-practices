def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x
        x = "inner"
        print(x)

    inner_function()
    print(x)


outer_function()
