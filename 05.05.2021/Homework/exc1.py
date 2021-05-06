# Utwórz dekorator @lowercase_decorator, który przyjmuje dowolną funkcję zwracającą łańcuch znaków
# i zwracający ten sam tekst zmieniony na małe litery.


def lowercase_decorator(function_passed):
    def wrapper():
        text_passed = function_passed()
        return text_passed.lower()

    return wrapper


@lowercase_decorator
def function_with_text():
    return "SAMPLE TEXT"


if __name__ == '__main__':
    print(function_with_text())
