# Utwórz klasę Pracownik.
#     Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#     Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
#     Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#     Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
#     Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#     Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com
#     tworzą adres mailowy. Np.
#           Adam Kowalski Love Python Company
#           email -> smkwlsk@lovepythoncompany.com
from dataclasses import dataclass


@dataclass
class Employee:
    position: str
    salary: float
    name: str
    surname: str
    work_experience: float
    is_student: bool

    def salary_up(self):
        self.salary += self.salary * .1 * round(self.work_experience)
        self.salary = round(self.salary, 5)

    def tax(self):
        if self.salary * 12 < 85528:
            return round((self.salary * 12) * 0.17, 3)
        elif self.is_student:
            print("Employee is student. Tax is 0.")
            return 0
        else:
            return round((self.salary * 12) * 0.32, 3)

    def sickness_contribution(self):
        if not self.is_student:
            self.salary -= 381.81
            print(f'Sickness salary is set to 381.81 PLN and subtracted from salary which is {self.salary}')
        else:
            print('Sickness contribution is 0 due to status of a student.')

    def show_info(self):
        mail = ""
        for i in range(len(self.name)):
            if self.name[i].lower() not in ('a', 'e', 'i', 'o', 'u'):
                mail += self.name[i]

        for i in range(len(self.surname)):
            if self.surname[i].lower() not in ('a', 'e', 'i', 'o', 'u'):
                mail += self.surname[i]

        introduction = f'{self.name} {self.surname} loves python company.'
        mail += "@lovespythoncompany.com"
        return introduction, mail


if __name__ == '__main__':
    emp1 = Employee("Developer", 5600, 'Adam', 'Kowalski', 1.3, True)
    emp1.salary_up()
    print(f'Tax: {emp1.tax()}')
    emp1.sickness_contribution()
    introduction, mail = emp1.show_info()
    print(introduction, f'\nemail -> {mail}')
