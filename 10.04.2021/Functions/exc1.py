# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
from math import pi


def calculate_radius_of_given_circle(radius: float) -> float:
    return round(pi * radius ** 2, 3)


print(calculate_radius_of_given_circle(4))
