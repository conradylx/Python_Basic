from Warrior import Warrior


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self._life = 40

    def attack(self):
        print(f"Archer: I let the arrow!")
        self._exp += 0.4


if __name__ == '__main__':
    object1 = Archer()
    print(object1)
    object1.march(110)
    print(object1)
    object1.attack()
    print(object1)
