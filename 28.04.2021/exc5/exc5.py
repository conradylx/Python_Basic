# Stwórz abstrakcyjną klasę Pojazdy.
# Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
# Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.
from abc import ABC, abstractmethod


class Vehicles(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def driving_licence(self):
        pass


class Car(Vehicles):
    def description(self):
        print("This is a car.")

    def driving_licence(self):
        print("You need licence category of B to drive this vehicle.")


class Bike(Vehicles):
    def description(self):
        print("This is a bike.")

    def driving_licence(self):
        print("You don't need any licence to drive this vehicle.")


class Bus(Vehicles):
    def description(self):
        print("This is a bus.")

    def driving_licence(self):
        print("You need licence category of C to drive this vehicle.")


class Truck(Vehicles):
    def description(self):
        print("This is a truck.")

    def driving_licence(self):
        print("You need licence category of C to drive this vehicle.")


if __name__ == '__main__':
    car = Car()
    car.description()
    car.driving_licence()
    bike = Bike()
    bike.description()
    bike.driving_licence()
    bus = Bus()
    bus.description()
    bus.driving_licence()
    truck = Truck()
    truck.description()
    truck.driving_licence()
