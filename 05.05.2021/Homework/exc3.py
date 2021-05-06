# Utwórz dekorator, który przyjmie funkcję zwracającą wartość liczbową BMI i zwraca tę samą
# wartość z informacją czy BMI jest prawidłowe

def check_bmi_decorator(function_passed):
    def wrapper():
        bmi_num = function_passed()
        if bmi_num > 30:
            return 'Obese'
        elif 25 <= bmi_num <= 29:
            return 'Overweight'
        elif 20 <= bmi_num <= 24:
            return 'Ideal'
        elif bmi_num < 18.5:
            return 'Underweight'

    return wrapper


@check_bmi_decorator
def get_bmi():
    return float(input("Enter BMI: "))


if __name__ == '__main__':
    print(get_bmi())
