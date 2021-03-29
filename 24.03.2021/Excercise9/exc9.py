# Korzystając z Google dowiedz się więcej o kodowaniu ASCII.
# Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość.
# Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII.
# Przykładowo literze A odpowiada numer 65. Zapoznaj się z metodami ord() oraz char().
# Pamiętaj o dodaniu znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość.
import csv


def code_word(word):
    with open("coded_word.txt", 'w', encoding='UTF-8') as file:
        for char in range(len(word)):
            file.write(str(ord(word[char]) + 1) + ";")


def decode():
    decoded_word = ""
    with open("coded_word.txt", "r", encoding='UTF-8') as coded_file:
        reader = csv.reader(coded_file, delimiter=';')
        for row in reader:
            for word in row:
                if word == '':
                    continue
                else:
                    decoded_word += chr(int(word) - 1)
    print(decoded_word)


word = input("Enter word to code: ")
code_word(word)
decode()
