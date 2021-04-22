# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.
from dataclasses import dataclass


@dataclass
class Orchid:
    color: str
    flowering_period: str
    species: str
    kingdom = "plant"

    def get_flower_color(self):
        print(f'Your flower is {self.color}.')

    def get_flower_period(self):
        print(f'Your flowering period is {self.flowering_period}.')

    def get_species(self):
        print(f'Your flower species is {self.species}.')


if __name__ == '__main__':
    flower1 = Orchid("Red", "Spring", "Lorien's flower")
    flower1.get_flower_color()
    flower1.get_flower_period()
    flower1.get_species()
    flower2 = Orchid("Yellow", "Spring", "Legolas's flower")
    flower2.get_flower_color()
    flower2.get_flower_period()
    flower2.get_species()
    flower3 = Orchid("Purple", "Summer", "Gimli's flower")
    flower3.get_flower_color()
    flower3.get_flower_period()
    flower3.get_species()


