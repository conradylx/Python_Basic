# Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.

def multiply_by_5_or_7(number, choice, sum):
    sum += choice
    if choice < number:
        return multiply_by_5_or_7(number, choice * 5, sum)
    elif choice == number:
        return sum
    else:
        sum -= choice
        return sum


def return_multi_by_5_or_7(number):
    sum = 0
    choice = int(input("Do you want sum multiply of 5 or 7? Enter 5 or 7\n"))
    while choice != 5 and choice != 7:
        choice = int(input(input("Enter 5 or 7: \n")))

    result = multiply_by_5_or_7(number, choice, sum)
    return result


if __name__ == '__main__':
    number = int(input("Enter N"))
    print(return_multi_by_5_or_7(number))
