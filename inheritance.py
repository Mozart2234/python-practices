class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.brand} {self.model} has been sold.")
        else:
            print(f"{self.brand} {self.model} is not available.")

    def check_availability(self):
        if self.is_available:
            print(f"{self.brand} {self.model} is available.")
        else:
            print(f"{self.brand} {self.model} is not available.")

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("This method must be implemented in the child class.")

    def stop_engine(self):
        raise NotImplementedError("This method must be implemented in the child class.")


class Car(Vehicle):
    def __init__(self, brand, model, price, color):
        super().__init__(brand, model, price)
        self.color = color

    def start_engine(self):
        print(f"{self.brand} {self.model} has started the engine.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} has stopped the engine.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, price, engine_type):
        super().__init__(brand, model, price)
        self.engine_type = engine_type

    def start_engine(self):
        print(f"{self.brand} {self.model} has started the engine.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} has stopped the engine.")


car = Car("Toyota", "Corolla", 25000, "Red")
motorcycle = Motorcycle("Honda", "CBR1000RR", 15000, "Inline-4")

motorcycle.start_engine()
motorcycle.stop_engine()

car.start_engine()
car.stop_engine()
