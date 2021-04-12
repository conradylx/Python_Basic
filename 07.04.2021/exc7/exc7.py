# Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby
# to użytkownik podawał nazwę pliku z cytatami. Pamiętaj, by użytkownik
# po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random


def read_from_file():
    while True:
        try:
            file_name = get_filename()
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = random.choice(file.readlines())
                print("Random quote:\n", data.center(150), "\n")
            break

        except (FileNotFoundError, FileExistsError):
            print("File not found")


def get_filename():
    return input("Enter file name: ")


if __name__ == '__main__':
    read_from_file()
