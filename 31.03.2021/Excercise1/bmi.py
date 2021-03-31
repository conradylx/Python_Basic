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


if __name__ == '__main__':
    print(calculate_BMI(80, 1.80))
