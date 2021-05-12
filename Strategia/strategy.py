from units.Archer import Archer
from units.Knight import Knight

if __name__ == '__main__':
    knights = list()
    archers = list()
    army = list()
    for unit in range(4):
        knights.append(Knight())

    for knight in knights:
        knight.march(2000)

    knights.append(Knight())
    for knight in knights:
        knight.attack()

    for unit in range(3):
        archers.append(Archer())
    army = knights + archers
    print(army)

    for warrior in army:
        warrior.attack()

    print(army)