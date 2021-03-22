# Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.
#     Pobierz imiona zakochanych
#     Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.
#     Redukuj liczbę elementów tablicy dodając pierwszą i ostatnią liczbę do siebie, tak długo, aż zostną dwie cyfry.
#     Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby.

def get_names():
    his_name = input("Enter his name: ").lower()
    her_name = input("Enter her name: ").lower()
    text_to_process = his_name + "loves" + her_name
    process_text(text_to_process)


def process_text(text: str):
    number = get_percentage_of_love(count_characters(text))
    while len(number) != 2:
        number = get_percentage_of_love(number)
    final = str(number[0]) + str(number[1])
    """Another solution is not concatenating two numbers into String, 
    but use subtraction of final from one hundred """
    # final = 100 - (number[0] + number[1])
    print(f"Love: {str(final)}%")


def count_characters(text: str) -> list:
    counted_characters = []
    counted_char_dict = {}

    """Count character without duplicates"""
    for char in text:
        if char in counted_char_dict:
            counted_char_dict[char] += 1
        else:
            counted_char_dict[char] = 1
    """Move values from dict to list"""
    for item in counted_char_dict.values():
        counted_characters.append(item)
    return counted_characters


def get_percentage_of_love(list_of_nums: list) -> list:
    temp_list = []
    for i in range(len(list_of_nums)):
        if len(list_of_nums) == 0:
            break
        if len(list_of_nums) >= 2:
            temp = list_of_nums.pop(0) + list_of_nums.pop(-1)
            temp_list.append(temp)
        elif len(list_of_nums) == 1:
            temp = list_of_nums.pop(0)
            temp_list.append(temp)
        else:
            temp_list.append(list_of_nums[0])
            break

    return temp_list


print("Welcome to 'the Love game'")
get_names()
