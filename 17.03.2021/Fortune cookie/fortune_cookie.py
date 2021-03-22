# Ciasteczko z wróżbą. Inspirując się typową facebookowa zabawą (https://tinyurl.com/y39uuf7n)
# poproś użytkownika o podanie daty urodzenia w dowolnym formacie, a następnie
# na podstawie miesiąca urodzenia przepowiedz mu co się wydarzy w nowym roku.

def process_user_input() -> tuple:
    user_birthday = input("Enter your birthday date [day month year]: ") \
        .replace('-', ' ') \
        .replace('.', ' ') \
        .replace('/', ' ') \
        .split()
    user_birthday = list(map(int, user_birthday))
    user_name = input("Enter your name: ")

    if user_birthday[1] > 12:
        print("Month cannot be greater than 12. Are you chinese or something?")
        quit()
    elif user_birthday[1] < 1:
        print("Month number is less than 1. Try again.")
        quit()
    if user_birthday[0] > 31:
        print("Day cannot be greater than 31. Are you using human calendar?")
        quit()
    elif user_birthday[0] < 1:
        print("Day number cannot be less than 1!")
        quit()

    return user_birthday, user_name


def predict_future(date: list, name: str):
    predictions = {
        1: "Marriage",
        2: "Love",
        3: "New car",
        4: "Lottery win",
        5: "You'll spend a lot of money for something",
        6: "You will meet someone special",
        7: "Broken leg",
        8: "Big surprise",
        9: "You will lose your best friend",
        10: "New bike",
        11: "New job",
        12: "Child born"
    }
    traits = {
        "A": "Spryciarz",       "L": "Perfekcjonista",
        "B": "Spóźnialski",     "M": "Czekoladoholik",
        "C": "Nerwus",          "N": "Wredota",
        "D": "Leniuszek",       "O": "Poważny",
        "E": "Kujon",           "P": "Nieogar",
        "F": "Pedant",          "R": "Źlośnik",
        "G": "Cwaniak",         "S": "Urodzony geniusz",
        "H": "Flirciarz",       "T": "Śpioch",
        "I": "Obibok",          "U": "Uparciuch",
        "J": "Szaleniec",       "W": "Śmieszek",
        "K": "Maniak selfie",   "Z": "Marzyciel",
    }

    if date[1] in predictions.keys():
        print(predictions.get(date[1]))
    else:
        print("You typed wrong month.")

    if name[0] in traits.keys():
        print(traits.get(name[0]))
    else:
        print("Something went wrong with your name. Are you sure that your first letter is alphabetical?")


birthday_date, user_name = process_user_input()
predict_future(birthday_date, user_name)
