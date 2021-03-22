# FLAMES to popularna gra, której nazwa postała od akronimu:
# Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
# Choć gra nie pozwala dokładnie przewidzieć przyszłości to może sprawdzić się jako andrzejkowa wróżba.

def start_game():
    """Main paragraph which is responsible for launching every function"""
    print('Welcome to the FLAMES game!')
    his_name, her_name = get_users_names()
    len_of_uncommon_chars = check_common_chars(his_name, her_name)
    relationship = analyze_relationship(len_of_uncommon_chars)
    get_score(his_name, her_name, relationship)


def get_users_names() -> tuple:
    """Paragraph to get names from user"""
    his_name = input("Enter his name: ").lower()
    her_name = input("Enter her name: ").lower()
    return his_name, her_name


def check_common_chars(his_name: str, her_name: str) -> int:
    """Paragraph responsible for removing common characters from both names"""
    my_str = ''
    """Check character for first str"""
    for char in his_name:
        if char not in her_name:
            my_str += char
    """Check character for second str"""
    for char in her_name:
        if char not in his_name:
            my_str += char
    return len(my_str)


def analyze_relationship(len_of_uncommon_chars: int):
    """Iterating over flame tuple to get character at len_of_uncommon position."""
    flame_tuple = ('F', 'L', 'A', 'M', 'E')
    word = ""
    final_index = 0
    for step in range(1, len_of_uncommon_chars):
        for index in range(1, len(flame_tuple)):
            if final_index == len_of_uncommon_chars:
                word = flame_tuple[index]
            final_index += 1
    return word


def get_score(his_name: str, her_name: str, relationship: str):
    """Last paragraph in the program. Compares argument with dictionary and displays proper value"""
    relationship_statuses = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
    }
    print(f'{his_name.capitalize()} and {her_name.capitalize()} will be {relationship_statuses.get(relationship)}')


start_game()
