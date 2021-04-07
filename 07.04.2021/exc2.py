# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd.

example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

user_index = int(input("Enter index in tuple: "))
tuple_value = input("Enter value to replace: ")

try:
    example_tuple[user_index] = tuple_value
except TypeError:
    print('Cannot replace value in tuple.')
except ValueError:
    print('Given index is string. Should be an integer.')