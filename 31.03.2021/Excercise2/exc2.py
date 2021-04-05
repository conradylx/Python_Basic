# Stwórz moduł, który przechowuje wzór na deltę.
# Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.
import math

from delta_module import calculate_delta


def enter_user_input():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    print(f'{a}x2 + {b}x + c')
    return a, b, c


def solve_delta(a, b, c):
    calculated_delta = calculate_delta(a, b, c)
    print(f'Delta is: {calculated_delta}')
    return calculated_delta


def find_solutions(delta, a, b):
    try:
        sol1 = round((-b - math.sqrt(delta)) / (2 * a), 2)
        sol2 = round((-b + math.sqrt(delta)) / (2 * a), 2)
        print(f'First solution: {sol1}\nSecond solution: {sol2}')
    except ValueError:
        print(f'Delta {delta} has no solutions.')


if __name__ == '__main__':
    a, b, c = enter_user_input()
    delta = solve_delta(a, b, b)
    find_solutions(delta, a, b)
