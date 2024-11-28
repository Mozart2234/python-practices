class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.available = True

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []

    def buy_car(self, car):
        if car.available:
            car.available = False
            self.cars.append(car)
            print(f"{self.name} bought {car.get_descriptive_name()}")
        else:
            print(f"{car.get_descriptive_name()} is not available")


class Agency:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.get_descriptive_name()} added to the inventory")

    def remove_car(self, car):
        self.cars.remove(car)
        print(f"{car.get_descriptive_name()} removed from the inventory")

    def show_inventory(self):
        print(f"{self.name} inventory:")
        for car in self.cars:
            print(f"\t- {car.get_descriptive_name()}")
