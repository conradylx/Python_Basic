# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
#         atrybuty: imię, kolor sierści, rasę
#
#         metody: szczekaj, machaj ogonem
#
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark():
        return 'hau'

    def wave(self):
        return 'waves'


dog1 = Dog('Dog1', 'breed1', 'brown')
dog2 = Dog('Dog2', 'Breed2', 'black')
print(dog1.name, dog1.color, dog1.breed, dog1.bark(), dog1.wave())
print(dog2.name, dog2.bark())
