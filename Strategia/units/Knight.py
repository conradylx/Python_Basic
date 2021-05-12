from Warrior import Warrior


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self._life = 60

    def attack(self):
        print(f"Knight: I swung my sword!")
        self._exp += 0.3


if __name__ == '__main__':
    object1 = Knight()
    print(object1)
    object1.march(110)
    print(object1)
    object1.attack()
    print(object1)
