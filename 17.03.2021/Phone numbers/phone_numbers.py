# Na wikipedii znajdują się informacje o numerach telefonów.
# Napisz program, który sprawdza czy podany przez użytkownika ciąg cyfr
# to numer telefonu oraz kraj do jakiego należy (program powinen zawierać przynajmniej 5 różnych krajów EU).
# Dla uproszczenia przyjmij:
# Główny numer składa się z 6 cyfr
# Numer zawsze podaje się w formacie międzynarodowym, a wiec musi zawierać prefix
# Międzynarodowy numer kierunkowy poprzedza się znakiem „+” (bez spacji) lub 00
def validate_number(phone_number: str):
    country = check_country(phone_number)
    is_valid_number = check_number(phone_number, country)
    return country, is_valid_number

def check_number(phone_number: str, country: str) -> bool:
    number_no_prefix = phone_number[3:].replace("-", "").replace(" ", "")
    country_number_len = {
        "Poland": 9,
        "Norway": 8,
        "Romania": 9,
        "Italy": 10,
        "France": 9,
    }
    if len(number_no_prefix) == country_number_len[country]:
        return True
    else:
        return False


def check_country(phone_number: str) -> str:
    country_codes = {
        "48": "Poland",
        "47": "Norway",
        "40": "Romania",
        "39": "Italy",
        "33": "France",
    }
    if phone_number[0:1] == "+" and country_codes.get(phone_number[1:3]):
        return country_codes.get(phone_number[1:3])
    elif phone_number[0:2] == "00" and country_codes.get(phone_number[2:4]):
        return country_codes.get(phone_number[2:4])
    else:
        print("Wrong country code.")
        quit()


phone_number = input("Enter phone number: ")
country, is_valid_number = validate_number(phone_number)
print(f"Number is from {country} and it's correctness is {is_valid_number}")
