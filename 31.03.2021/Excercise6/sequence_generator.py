#     Utwórz generator instancji testowych, który wygeneruje losowe
#     ciągi znaków składające się z jedynie z cyfr od 0-9.
#         Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
#     Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika
#         np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
#     Zaimportuj generator bezpośrednio do programu.

from random import randrange, choice


def generate_numeric_string(user_input: str) -> str:
    random_len = randrange(50)
    digital_string = ""

    if len(user_input) == 0:
        for digit in range(random_len):
            digital_string += str(randrange(10))
    else:
        for digit in range(random_len):
            digital_string += str(choice(user_input))

    return digital_string


if __name__ == '__main__':
    print(generate_numeric_string('text'))
