# Stwórz grę wisielec “bez wisielca”.
#     Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#     Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#     Użykownik podaje literę.
#     Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
#             “Trafione!” oraz napis ze znanymi literami.
#     W przeciwnym wpadku pokaż komunikat:
#             “Nie trafione, spróbuj jeszcze raz!”.
#     Możesz ograniczyć liczbę prób do np. 10.
import random


def take_random_words(words: list) -> list:
    return random.choice(words)


def play_rounds(word):
    word_length = len(word)
    spare_guesses = 5
    print('Guess hidden word')
    hidden_word = '_' * word_length
    guessed = False
    print(hidden_word)

    for round in range(0, word_length + spare_guesses):
        user_guess = input("Enter a character ")
        if user_guess not in word:
            print(f"{user_guess} not found in the word. {(word_length + spare_guesses) - round} guesses left.")
        else:
            for index in range(len(word)):
                if word[index] == user_guess:
                    hidden_word = hidden_word[:index] + user_guess + hidden_word[index + 1:]
        print(hidden_word)

        if '_' not in hidden_word:
            print('Password is guessed')
            guessed = True
            break

    if guessed == False:
        print(f'0 guesses left.\n Hidden word was: {word}')



list_of_words = [
    'komputer', 'losuje', 'wyraz', 'lista', 'samochod',
    'uzytkownik', 'zamaskowany', 'widoczna', 'liczba',
    'ziemniak', 'pomidor', 'papryka', 'rycerz', 'rower',
    'ziemianin', 'polka', 'myszka', 'papuga', 'pies', 'karolina'
]
random_word = take_random_words(list_of_words)
# print(random_word)
play_rounds(random_word)
