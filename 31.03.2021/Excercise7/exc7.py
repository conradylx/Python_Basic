# Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.

from fibonnaci import calc_fibonnaci_numbers

if __name__ == '__main__':
    nth_number = int(input('Enter nth fibonacci number: '))

    print(calc_fibonnaci_numbers(nth_number))
