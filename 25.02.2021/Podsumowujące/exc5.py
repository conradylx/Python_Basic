# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

secret_number = random.randint(1, 100)
steps = 0
print(secret_number)

while steps < 6:
    user_guess = input("Enter number: ")

    '''Check if given guess is numeric. If not then convert input to integer'''
    if user_guess.isalpha():
        print("Value is not numeric. Try again!")
        continue
    else:
        user_guess = int(user_guess)

    '''Check distance to secret_number'''
    distance = abs(secret_number - user_guess)

    if user_guess == secret_number:
        print("Correct!")
        break
    elif distance < 15:
        print("Warm")
    else:
        print("Cold")
    steps += 1
