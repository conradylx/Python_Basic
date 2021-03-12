# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał
# co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że
# rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania
# samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

import datetime


def check_if_car_is_antique(data: dict):
    print(data)
    actual_year = datetime.datetime.now()
    car_age = 0
    if data['year'] > actual_year.year:
        print("Nieprawidłowy rocznik samochodu.")
    else:
        car_age = actual_year.year - data['year']

    if car_age >= 25 and data["is_original"] == True:
        print(f'Gratulacje! Twój samochód {data["mark"]} może być zarejestrowany jako zabytek.')
    elif car_age >= 25 and data["is_original"] == False:
        print(f'Twój samochód {data["mark"]} nie może być zarejestrowany jako zabytek z powodu nieoryginalnych części.')
    elif car_age < 25 and data["is_original"] == False:
        print(f'Twój samochód {data["mark"]} nie może być zarejestrowany jako zabytek z '
              f'powodu nieoryginalnych części i wieku samochodu.')
    else:
        print(f'Twój samochód {data["mark"]} jest jeszcze zbyt młody.')


car_details = {"mark": "Opel", "model": "Astra", "year": 1995, 'is_original': True}
check_if_car_is_antique(car_details)
