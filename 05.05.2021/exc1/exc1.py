# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch
# znaków i zwracający ten sam tekst zmieniony na wielkie litery.

def uppercase_decorator(f):
    def uppercase_method():
        text_to_format = f()
        print(text_to_format.upper())

    return uppercase_method


@uppercase_decorator
def function_with_text():
    return "sample text"


if __name__ == '__main__':
    function_with_text()
