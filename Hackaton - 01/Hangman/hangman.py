import random
import json


def take_random_words(words: list):
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


def get_data_from_file():
    with open('hangman.json') as json_file:
        data = json.load(json_file)
    return data


def get_category_from_user(list_of_words):
    categories = ""
    for key, value in list_of_words.items():
            categories = categories + key + " "

    user_category = input(f"Wybierz jedną kategorię: {categories} ").capitalize()
    data_from_json = dict()

    for key, value in list_of_words.items():
        if key == user_category:
            data_from_json[key] = value
    data_from_json = list(*data_from_json.values())
    return data_from_json



list_of_words = get_data_from_file()
category_words = get_category_from_user(list_of_words)
random_word = take_random_words(category_words)
play_rounds(random_word.lower())
