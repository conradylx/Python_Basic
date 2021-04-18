# Napisz funkcję przeszukiwania połówkowego (binarenego), która
# przyjmuje dwa parametry - szukany element oraz listę elementów.
# Zwraca informację czy element jest obecny na liście, albo nie.


def check_if_list_contains(list_of_words, word):
    list_of_words.sort()
    min_len = 0
    max_len = len(list_of_words) - 1

    while min_len <= max_len:
        mid_len = (min_len + max_len) // 2
        guess = list_of_words[mid_len]
        if guess == word:
            return True
        if guess < word:
            min_len = mid_len + 1
        else:
            max_len = mid_len - 1
    return False


if __name__ == '__main__':
    list_of_words = ["Ala", "ma", 'kota', "który", "śpi"]
    print(check_if_list_contains(list_of_words, "kota"))
    print(check_if_list_contains(list_of_words, "Filemona"))
