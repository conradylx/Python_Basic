# Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

example_list = [1.2, 1, 'hello', [], False, {'hello': 123}, ()]

given_index = int(input('Enter index: '))

try:
    result = 1 / example_list[given_index]
    print(result)
except ValueError as error:
    print(error)
except TypeError:
    print('Cannot divide by other type than int or float.')
except IndexError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)