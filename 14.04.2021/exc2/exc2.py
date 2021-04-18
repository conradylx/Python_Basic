# Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.

def addition_by_number(number, add_by_num, temp_sum, sum_of_nums):
    if temp_sum < number:
        return addition_by_number(number, add_by_num, temp_sum+add_by_num, sum_of_nums+temp_sum)
    else:
        return sum_of_nums


def return_multi_by_5_or_7(number):
    addition_number = 5
    sum_of_5s = addition_by_number(number, addition_number, 0, 0)
    addition_number = 7
    sum_of_7s = addition_by_number(number, addition_number, 0, 0)
    return sum_of_5s + sum_of_7s


if __name__ == '__main__':
    number = int(input("Enter N"))
    print(return_multi_by_5_or_7(number))
