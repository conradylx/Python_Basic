# Utwórz dekorator @randomcase_decorator, który przyjmuje dowolną funkcję zwracającą łańcuch znaków
# i zwracający ten sam tekst zmieniony na duże i małe litery w dowolnej kolejności np.
from random import randrange


def randomcase_decorator(function_passed):
    def wrapper():
        text_passed = function_passed()
        new_text = ""
        for character in range(len(text_passed)):
            random_num = randrange(10)
            if random_num < 5:
                new_text += text_passed[character].upper()
            else:
                new_text += text_passed[character]
        return new_text

    return wrapper


@randomcase_decorator
def function_with_text():
    return "lorem ipsum dolor sit amet"


if __name__ == '__main__':
    print(function_with_text())
