# Create a Car class with brand, model, and a drive() method.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

# Example usage
car1 = Car("Toyota", "Corolla")
car1.drive()