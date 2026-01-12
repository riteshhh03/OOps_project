# Parent Class
class Vehicle:
    def __init__(self, name, rent):
        self.name = name
        self._rent = rent      # Encapsulation
        self.available = True

    def calculate_rent(self, days):
        return self._rent * days


# Child Class
class Car(Vehicle):
    def calculate_rent(self, days):
        return self._rent * days   # Polymorphism


class Bike(Vehicle):
    def calculate_rent(self, days):
        return (self._rent * days) - 100   # Discount


# Customer Class
class Customer:
    def __init__(self, name):
        self.name = name

    def rent_vehicle(self, vehicle, days):
        if vehicle.available:
            vehicle.available = False
            print(f"{self.name} rented {vehicle.name}")
            print("Total Rent:", vehicle.calculate_rent(days))
        else:
            print("Vehicle not available")


# Actual Main Program
car = Car("Toyota", 2000)
bike = Bike("Yamaha", 800)

customer = Customer("Ritesh")

customer.rent_vehicle(car, 2)
customer.rent_vehicle(bike, 3)
