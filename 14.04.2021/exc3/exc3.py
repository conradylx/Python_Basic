# Przypomnij sobie szkolny wzór na silnię.
# Zapisz funkcję silnia iteracyjnie np. pętlą for, a
# następnie analogiczną funkcję tylko, że rekurencyjnie.


def factorial_by_loop(number):
    sum = 1
    for index in range(1, number + 1):
        sum *= index
    return sum


def factorial_by_recursion(number):
    if number == 1:
        return 1
    else:
        return number*factorial_by_recursion(number-1)


if __name__ == '__main__':
    number = int(input("Enter N: "))
    print(factorial_by_loop(number))
    print(factorial_by_recursion(number))
