import math


def calculate_circle_area(r: int) -> int:
    return math.pi * r ** 2


def calculate_rectangle_area(a: int, b: int) -> int:
    return a * b


def calculate_trapeze_area(a: int, b: int, h: int) -> float:
    return ((a + b) * h) / 2


if __name__ == '__main__':
    print(calculate_circle_area(10))
    print(calculate_rectangle_area(10, 10))
    print(calculate_trapeze_area(10, 10, 4))
