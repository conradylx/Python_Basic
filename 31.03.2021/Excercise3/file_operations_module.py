# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób
# odczytu oraz bezpieczny zapis. Funkcja czytająca pliki sprawdza najpierw czy dany
# plik istnieje oraz czy jest niepusty. Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
import os


def safe_read_file(filename):
    try:
        with open(filename, mode='r', encoding='UTF-8') as file:
            file_size = os.stat(filename)
            if file_size.st_size == 0:
                return "File is empty"
            reader = file.read()
            return reader
    except FileNotFoundError:
        return "File not found."


def save_write_to_file(filename):
    text_to_file = "Sample text to write"
    try:
        with open(filename, mode='w', encoding='UTF-8') as file:
            file_size = os.stat(filename)
            if file_size.st_size != 0:
                return "File is not empty"
            file.write(text_to_file)
            return "File saved."
    except FileExistsError:
        return "File found."


if __name__ == '__main__':
    print(safe_read_file('text.txt'))
    print(save_write_to_file('text.txt'))
