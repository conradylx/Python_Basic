# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#     Program zacznie ze stworzonym słownikiem o trzech kluczach:
#             marka (str)
#             model (str)
#             rocznik (int)
#     Wypisze ten słownik na ekran (bez żadnego formatowania)
#     Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#         “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#     Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#         “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#     Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
#     aby zobaczyć, czy progam również zmienia swoje zachowanie.
import datetime


def check_if_car_is_antique(data: dict):
    print(data)
    actual_year = datetime.datetime.now()
    car_age = 0
    if data['year'] > actual_year.year:
        print("Nieprawidłowy rocznik samochodu.")
    else:
        car_age = actual_year.year - data['year']

    if car_age >= 25:
        print(f'Gratulacje! Twój samochód {data["mark"]} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {data["mark"]} jest jeszcze zbyt młody.')


car_details = {"mark": "Opel", "model": "Astra", "year": 1990}
check_if_car_is_antique(car_details)
