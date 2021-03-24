import random


def read_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            data = random.choice(file.readlines())
            print("Random quote:\n", data.center(150), "\n")

    except FileNotFoundError:
        print("File not found")


def append_to_file(file_name):
    try:
        with open(file_name, 'a+', encoding='UTF-8') as file:
            data = file.write("\nAuthor: Cicero")
            file.seek(0)
            print(file.read())

    except FileNotFoundError:
        print("File not found")


file_name = input("Enter file name: ")
read_from_file(file_name)
append_to_file(file_name)
