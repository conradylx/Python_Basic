# W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ?
# Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.


def calculate_BMI(mass: int, height: float) -> str:
    bmi = mass / (height ** 2)
    bmi_rounded = round(bmi, 2)

    if bmi_rounded < 18:
        return "Niedowaga"
    elif 18 <= bmi_rounded < 25:
        return "Waga_normalna"
    elif 25 <= bmi_rounded < 30:
        return "Nadwaga"
    elif bmi_rounded >= 30:
        return "Otyłość"


def main_function():
    mass, height = get_input_data()
    bmi_result = calculate_BMI(mass, height)
    print_advice(bmi_result)


def get_input_data() -> tuple:
    mass, height = 0, 0.0
    while True:
        try:
            mass = float(input('Podaj swoją wagę w kg (np 80): '))
            height = float(input('Podaj swój wzrost w metrach (np 1.80): '))
        except(ValueError, TypeError):
            print('This is not valid value. Try again')

        if mass > 30 and 1.5 < height < 2.35:
            break
        else:
            if 1.5 < height < 2.35:
                print('Your height is too high. Try again.')
            elif not (mass > 30 and 1.5 < height < 2.35):
                print('Your height is too high and mass is too low. Try again.')
            else:
                print('Your mass is too low. Try again.')

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
