import random

from PersonClass import Person


class Elf(Person):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.race = "Elf"
        self.offence = 33
        self.defence = 7
        self.inventory = ["Bow"]


class Dwarf(Person):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.race = "Dwarf"
        self.offence = 15
        self.defence = 25
        self.inventory = ["Axe"]


class Human(Person):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.race = "Human"
        self.offence = 20
        self.defence = 20
        self.inventory = ["Sword"]


class Ork(Person):
    def __init__(self):
        super().__init__(self)
        self.race = "Ork"
        self.offence = random.randint(1, 40)
        self.defence = random.randint(1, 40)
        self.inventory = ["Mace"]
