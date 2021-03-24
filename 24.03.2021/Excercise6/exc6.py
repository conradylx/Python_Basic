#  Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
#  Sprawdź dla każdej kart jej typ.
#  Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

def read_cards_numbers(filename: str) -> list:
    with open(filename) as fp:
        content = fp.readlines()
    return content


def save_card_data_to_file(card_name: str, number: int):
    file_name = f'{card_name}.txt'
    with open(file_name, encoding='UTF-8', mode='w') as file:
        file.write(str(number))


def walidation_of_cards(numbers: list):
    for number in numbers:
        number = number.replace(" ", "").replace("\n", "")
        if len(str(number)) == 13:
            check_if_visa_card(number)
        elif len(str(number)) == 15:
            check_if_american_express(number)
        elif len(str(number)) == 16:
            check_if_mastercard(number)
            check_if_visa_card(number)


def check_if_mastercard(number: int):
    number_to_str = str(number)
    if (51 <= int(number_to_str[:2]) <= 55) or (2221 <= int(number_to_str[:2]) <= 2720):
        print(f'Number {number} belongs to Mastercard')
        save_card_data_to_file('mastercard', number)


def check_if_visa_card(number: int):
    number_to_str = str(number)
    if int(number_to_str[:1]) == 4:
        print(f'Number {number} belongs to Visa Card')
        save_card_data_to_file('visa', number)


def check_if_american_express(number):
    number_to_str = str(number)
    if int(number_to_str[:2]) == 34 or int(number_to_str[:2]) == 37:
        print(f'Number {number} belongs to American Express')
        save_card_data_to_file('american_express', number)


cards = read_cards_numbers('card_numbers.txt')
walidation_of_cards(cards)
