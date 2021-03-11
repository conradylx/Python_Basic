# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random


def get_user_input():
    secret_number = random.randint(1, 50)
    steps = 0
    print(secret_number)
    correct = False

    while steps < 10 and correct == False:
        user_guess = input("Enter number: ")

        '''Check if given guess is numeric. If not then convert input to integer'''
        if user_guess.isalpha():
            print("Value is not numeric. Try again!")
            continue
        else:
            user_guess = int(user_guess)

        correct = print_tips(secret_number, user_guess)
        steps += 1


def print_tips(secret_number, user_guess):
    '''Check distance to secret_number'''
    distance = abs(secret_number - user_guess)
    correct = False

    if user_guess == secret_number:
        print("Correct!")
        correct = True
    elif distance <= 5:
        print("Hot")
    elif distance < 15:
        print("Warm")
    else:
        print("Cold")

    return correct


get_user_input()
