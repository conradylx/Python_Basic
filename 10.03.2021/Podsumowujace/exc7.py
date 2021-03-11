# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z
# Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
# All have 16 digits.
#     American Express card numbers start with 34 or 37 and have 15 digits.
# American express: 378282246310005
# Visa: 4111111111111111
# Mastercard: 5555555555554444

def walidation_of_cards(number: int):
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


def check_if_visa_card(number: int):
    number_to_str = str(number)
    if int(number_to_str[:1]) == 4:
        print(f'Number {number} belongs to Visa Card')


def check_if_american_express(number):
    number_to_str = str(number)
    if int(number_to_str[:2]) == 34 or int(number_to_str[:2]) == 37:
        print(f'Number {number} belongs to American Express')


card_number = 378282246310005
walidation_of_cards(card_number)
