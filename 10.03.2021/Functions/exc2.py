# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def check_if_number_is_even(number: int):
    if number % 2 == 0:
        print(f'Number {number} is even')
    else:
        print(f'Number {number} is odd')


given_number = int(input("Enter a number "))
check_if_number_is_even(given_number)