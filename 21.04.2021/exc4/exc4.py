# Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.
from abc import abstractmethod


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def say_something(self):
        pass


class Wolf(Animal):
    def say_something(self):
        print("I am a wolf!")


class Horse(Animal):
    def say_something(self):
        print("I am a horse!")


if __name__ == '__main__':
    horse = Horse("Black", "Jack")
    horse.say_something()
    wolf = Wolf("Grey", "Earl")
    wolf.say_something()
