# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def main_function():
    mass, height = get_input_data()
    calculated_bmi = calculate_BMI(mass, height)
    print_final_result(calculated_bmi)


def get_input_data() -> tuple:
    mass = int(input('Podaj swoją wagę w kg (np 80): '))
    height = float(input('Podaj swój wzrost (np 1.80): '))
    return mass, height


def calculate_BMI(mass: int, height: int) -> int:
    BMI = mass / (height ** 2)
    BMI_rounded = round(BMI, 2)
    print('Moje BMI ', BMI_rounded)
    return BMI_rounded


def print_final_result(BMI_rounded: int) -> None:
    if BMI_rounded < 16:
        print("Niedowaga")
    elif BMI_rounded >= 16 and BMI_rounded < 25:
        print("Waga normalna")
    elif BMI_rounded >= 25 and BMI_rounded < 30:
        print("Nadwaga")
    elif BMI_rounded >= 30:
        print("Otyłość")


main_function()