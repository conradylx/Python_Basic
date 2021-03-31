#     Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py.
#     Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika
#     o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość)
#     sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
#     1) Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości:
#           niedowaga, waga normalna, nadwaga, otyłość.
#     2) Utwórz 4 pliki .txt zawierające porady.
#     3) Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
#           fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
#     4) Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.

from bmi import calculate_BMI


def main_function():
    mass, height = get_input_data()
    bmi_result = calculate_BMI(mass, height)
    print_advice(bmi_result)


def get_input_data() -> tuple:
    mass = int(input('Podaj swoją wagę w kg (np 80): '))
    height = float(input('Podaj swój wzrost (np 1.80): '))
    return mass, height


def print_advice(bmi_result):
    try:
        with open(f'{bmi_result}.txt', mode="r", encoding="utf8") as file:
            reader = file.read()
            print(reader)
    except FileNotFoundError:
        print("Something went wrong.")


if __name__ == '__main__':
    main_function()
