# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
guess = 0

while guess != secret_num:
    guess = int(input("Enter secret number: "))
    print("Correct answer!") if guess == secret_num else print("Incorrect! Try again! ")
