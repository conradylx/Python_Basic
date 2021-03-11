# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def find_max(numbers):
    list_len = len(numbers)
    for i in range(list_len - 1):
        for j in range(0, list_len - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = numbers[j]
    return numbers[0]


list_of_numbers = [12, 22, 3, 22, 55, 4, 12, 45, 89]
final = find_max(list_of_numbers)
print(final)