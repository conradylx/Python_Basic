# W pierwszym wierszu standardowego wejścia zapisano liczbę nazwisk N(1<= N <= 200).
# W następnych N wierszach zapisano po jednym nazwisku. Nazwisko rozpoczyna wielką litera,
# jego długość nie przekracza 50 znaków, i składa się tylko z liter alfabetu angielskiego.

def get_data_from_file() -> tuple:
    with open('data_list.txt', 'r', encoding='UTF-8') as file:
        length_from_file = file.readline()
        surnames_data = file.readlines()
    surnames = [x.replace('\n', '') for x in surnames_data]
    return length_from_file, surnames


def retrieved_data_validation(data_len: int, data_list: list):
    total_records = len(data_list)
    if total_records != int(data_len):
        print(f'Total records in file {total_records}, but should be {data_len} as declared.')
        quit()
    data_list.sort()

    for surname in data_list:
        if not surname.isalpha():
            print(f'{surname} has not allowed character such like numbers.')
            quit()
        elif len(surname) > 50:
            print(f'{surname} len is above 50.')
            quit()
        print(surname)


if __name__ == '__main__':
    surname_len, surname_list = get_data_from_file()
    retrieved_data_validation(surname_len, surname_list)
