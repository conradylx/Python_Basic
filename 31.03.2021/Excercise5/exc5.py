# Stwórz moduł obliczający pola różnych figur.
# W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów
# pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku.

from math_figures_calculate import calculate_circle_area, calculate_rectangle_area, calculate_trapeze_area

a, b, h, r = 10, 5, 9, 7

shape = input('Enter shape: [circle, rectangle, trapeze]: ')
if shape == 'trapeze':
    print(round(calculate_trapeze_area(a, b, h), 2))
elif shape == 'rectangle':
    print(calculate_rectangle_area(a, b))
elif shape == 'circle':
    print(round(calculate_circle_area(r), 2))
else:
    print('Shape not found')
