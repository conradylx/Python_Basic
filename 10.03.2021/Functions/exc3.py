# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def calculate_sum_of_numbers(array: list) -> int:
    final = 0
    for number in array:
        final += number

    return final


list_of_numbers = [1, 2, 3, 4]
final_score = calculate_sum_of_numbers(list_of_numbers)
print(final_score)
