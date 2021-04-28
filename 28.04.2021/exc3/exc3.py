# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.
from dataclasses import dataclass


@dataclass
class Pen:
    __name: str = "Pen"

    def get_name(self):
        return self.__name


@dataclass
class Pinapple:
    __name: str = "Pinapple"

    def get_name(self):
        return self.__name


class PenPinapple(Pinapple, Pen):
    def __init__(self):
        self.pen_name = Pen.get_name(self)
        self.pinapple_name = Pinapple.get_name(self)

    def print_name(self):
        return self.pinapple_name + self.pen_name


if __name__ == '__main__':
    c1 = PenPinapple()
    print(c1.print_name())
