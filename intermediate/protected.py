class BaseClass:
    def __init__(self) -> None:
        self._protected = "protected"
        self.__private = "private"

    def _protected_method(self):
        return "protected method"

    def __private_method(self):
        return "private method"

    def print_private(self):
        return self.__private


object = BaseClass()
print(object._protected_method())
print(object._protected)

print(object.print_private())
