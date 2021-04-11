class Person:
    def __init__(self, name):
        self.name = name
        self.race = ""
        self.health = 100
        self.offence = 10
        self.defence = 5
        self.inventory = []

    def attack(self, target):
        if target.defence > self.offence:
            print("Defence is much more better! Miss! ")
        else:
            target.health -= abs(target.defence - self.offence)

    def defence(self, agressor):
        if agressor.offence < self.defence:
            print("Defence is much more better than enemy's attack!")
        else:
            self.health -= abs(agressor.offence - self.defence)


if __name__ == "__main__":
    hero = Person("1")
    hero2 = Person("2")
    hero.attack(hero2)
    print(hero2.health)
