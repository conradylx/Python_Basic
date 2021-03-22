# Program loteria. Użytkownik, podobnie jak w klasycznym totolotku,
# podaje ciąg 6 swoich liczb w zakresie od 1 do 50. Komputer losuje 6 liczb totolotka.
# Wygrana zależy od tego ile cyfr zostało trafionych przez użytkownika
import random


def input_data_validation() -> list:
    numbers = input("Enter 6 numbers from 1 to 50: ").split(" ")
    numbers = list(map(int, numbers))
    numbers_digits = dict()

    if len(numbers) < 6 or len(numbers) > 6:
        print("You need to input only 6 numbers. Try again.")
        quit()

    for number in numbers:
        if number > 50 or number < 1:
            print("Wrong range of numbers. You can type numbers from 1 to 50 only. Try again.")
            quit()
        if number not in numbers_digits:
            numbers_digits.update({number: number})
        else:
            print(f'{number} is duplicated. Try type another numbers.')
            quit()
    return numbers


def start_lottery(user_numbers):
    lottery_numbers = list(range(1, 50))
    guessed_numbers = 0
    random.shuffle(lottery_numbers)
    lottery_numbers = lottery_numbers[:6]
    win_data_tuple = (('I', 6, 1000000), ('II', 5, 3500), ('III', 4, 100), ('IV', 3, 10))

    for number in user_numbers:
        if number in lottery_numbers:
            guessed_numbers += 1

    if guessed_numbers == win_data_tuple[0][1]:
        print(f'You have {win_data_tuple[0][0]} degree win. Amount of win is equal {win_data_tuple[0][2]} PLN')
    elif guessed_numbers == win_data_tuple[1][1]:
        print(f'You have {win_data_tuple[1][0]} degree win. Amount of win is equal {win_data_tuple[1][2]} PLN')
    elif guessed_numbers == win_data_tuple[2][1]:
        print(f'You have {win_data_tuple[2][0]} degree win. Amount of win is equal {win_data_tuple[2][2]} PLN')
    elif guessed_numbers == win_data_tuple[3][1]:
        print(f'You have {win_data_tuple[3][0]} degree win. Amount of win is equal {win_data_tuple[3][2]} PLN')
    else:
        print('Try your luck in the next lottery!')


validated_data = input_data_validation()
start_lottery(validated_data)
