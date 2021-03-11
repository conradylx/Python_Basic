# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.


def check_if_number_is_in_range(number, left, right):
    if left <= number <= right:
        print('It is')
    else:
        print("Is not")


number = int(input("Enter number "))
range_left = int(input("Enter range from left "))
range_right = int(input("Enter range from right "))
check_if_number_is_in_range(number, range_left, range_right)