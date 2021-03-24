# Wyświetl tylko 5 pierwszych linii

def read_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            for line in range(5):
                print(file.readline())
    except FileNotFoundError:
        print("File not found")


read_from_file('text.txt')
