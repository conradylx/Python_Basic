# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def check_if_number_is_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f'Number {number} is even')


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
check_if_number_is_even(number_list)
