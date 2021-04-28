# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
# Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
# Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.

class Animals:
    def __init__(self):
        print("Hello from Animals class")


class Mammals(Animals):
    def __init__(self):
        super().__init__()
        print("Hello from Mammals class")

    def example_text(self):
        print("Simple example text")


class Cat(Mammals):
    def __init__(self):
        super().__init__()
        print("Hello from Cat class")


class Dog(Mammals):
    def __init__(self):
        super().__init__()
        print("Hello from Dog class")


class Human(Mammals):
    def __init__(self):
        super().__init__()
        print("Hello from Human class")


if __name__ == '__main__':
    cat = Cat()
    print('------------------------')
    dog = Dog()
    print('------------------------')
    human = Human()
    human.example_text()
