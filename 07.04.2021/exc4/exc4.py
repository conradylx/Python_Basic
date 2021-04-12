# Oblicz średnią arymetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def decorator(func):
    def wrapper():
        print('-------------------------------------------------------------')
        func()
        print('-------------------------------------------------------------')

    return wrapper


@decorator
def message():
    print("Error. Check if you gave non-numeric character and try again.")


def save_into_file(error):
    with open('errors.txt', mode='w', encoding='utf-8', ) as error_file:
        error_file.write(str(error))


def get_input():
    is_error = True
    numbers = list()
    while is_error:
        numbers = input("Enter numbers in line seperating them by ',' :")
        numbers = list(numbers.split(','))
        try:
            for i, v in enumerate(numbers):
                numbers[i] = int(v)
                is_error = False
        except (ValueError, TypeError, EOFError) as error:
            message()
            save_into_file(error)
            is_error = True

    return numbers


def calculate_average(numbers):
    num_length = len(numbers)
    num_sum = sum(numbers[:num_length])
    average = num_sum / num_length
    return average


if __name__ == '__main__':
    numbers = get_input()
    print(calculate_average(numbers))
