import json
import random
import time

from turtle_draw import print_hangman


def take_random_words(words: list) -> list:
    """
    Function returns random word from given argument list.
    """
    return random.choice(words)


def play_rounds(word: list):
    """
    Main logic function.
    """
    word_length = len(word)
    list_of_typed_chars = []
    guesses = 7
    print('Guess hidden word')
    hidden_word = '_' * word_length
    change_hangman_color = False
    hangman_counter = 0
    print(hidden_word)

    for iteration in range(word_length + guesses):
        user_guess = check_if_char_typed(list_of_typed_chars)

        if user_guess not in word:
            hangman_counter += 1
            guesses -= 1
            print(f"{user_guess} not found in the word. {guesses} guesses left.")
            if guesses == 0:
                print(f'Game is over. Hidden word was: {word}')
                change_hangman_color = True
                print_hangman(hangman_counter, change_hangman_color)
                time.sleep(4)  # time sleep inside print_hangman doesnt work because of break below so I put it here.
                break
            else:
                print_hangman(hangman_counter, change_hangman_color)
        else:
            for index in range(len(word)):
                if word[index] == user_guess:
                    hidden_word = hidden_word[:index] + user_guess + hidden_word[index + 1:]
        print(hidden_word)

        if '_' not in hidden_word:
            print('Password is guessed')
            break


def check_if_char_typed(list_of_typed_chars: list) -> str:
    """
    Function checks if given character is already typed.
    """
    user_guess = input("Enter a character ")
    if user_guess in list_of_typed_chars:
        char_in_list = True
    else:
        list_of_typed_chars.append(user_guess)
        char_in_list = False

    while char_in_list:
        user_guess = input("Already typed that character.\nEnter another character ")
        if user_guess not in list_of_typed_chars:
            list_of_typed_chars.append(user_guess)
            char_in_list = False
    return user_guess


def get_data_from_json_file() -> list:
    try:
        with open('words.json', mode='r', encoding='UTF-8') as json_file:
            data = json.load(json_file)
        data_from_json = list(*data.values())
        return data_from_json
    except (FileExistsError, FileNotFoundError):
        print("JSON file not found.")
        quit()


if __name__ == '__main__':
    list_of_words = get_data_from_json_file()
    random_word = take_random_words(list_of_words)
    play_rounds(random_word)
