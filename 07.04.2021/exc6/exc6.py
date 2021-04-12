# Wywołaj błąd związany z otwarciem pliku.
#     Spróbuj odczytać plik, który nie istnieje.
#     Spróbuj odczytać wartość z pliku otwartym w trybie w
#     Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.
from io import UnsupportedOperation


def log_errors(error):
    with open("errors.txt", mode="a", encoding="UTF-8") as logfile:
        logfile.write(str(error))


def open_non_exist_file():
    try:
        with open("Tom_Bombadils_tale1.txt", mode='r', encoding='UTF-8') as tale:
            tale.read()
    except (FileExistsError, FileNotFoundError, TypeError) as error:
        log_errors(error)
        print("File does not exist.")
        quit()


def read_from_write_file():
    try:
        with open("Tom_Bombadils_tale2.txt", mode='w', encoding='UTF-8') as tale:
            tale.read()
    except (UnsupportedOperation) as error:
        log_errors(error)
        print("Cannot read from file which is opened in write mode.")
        quit()


def create_existing_file():
    try:
        with open("Tom_Bombadils_tale2.txt", mode='w', encoding='UTF-8') as tale:
            tale.read()
    except (UnsupportedOperation) as error:
        log_errors(error)
        print("Cannot create file which is already exist.")
        quit()


if __name__ == '__main__':
    # open_non_exist_file()
    # read_from_write_file()
    create_existing_file()
