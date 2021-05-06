# Utwórz klasę Robot każdy robot ma imię i rok produkcji. Utwórz właściwość, która zwraca kondycję robota (condition).
# Kondycja jest liczona jako suma cyfr składających się na rok produkcji np. (1973 = 20, 1993 = 22,  2020 = 4 etc).
# Jeśli suma cyfr jest poniżej 5 zwróć tekst ‘seems ok!’, dla wartości 5 - 10 - ‘honestly could be better;
# 10 - 15  ‘bad choice’, 15 w górę ’cheap & weak’.

class Robot(object):

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.__condition = 0

    def calculate_condition(self):
        year_check = list(str(self.year))
        if len(year_check) != 4:
            return "Invalid year of production!"
        for i in range(0, len(year_check)):
            year_check[i] = int(year_check[i])
        self.__condition = sum(year_check)

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition):
        self.__condition = condition

    @staticmethod
    def check_condition(condition):
        if condition < 5:
            return "Seems ok"
        elif 5 <= condition < 10:
            return "Honestly could be better"
        elif 10 <= condition < 15:
            return "Bad choice"
        elif 15 <= condition > 20:
            return "Cheap & weak"


if __name__ == '__main__':
    r1 = Robot('R1', 2020)
    print('Condition before change:', r1.condition)
    r1.condition = 3
    print('Condition after change:', r1.condition)
    r1.calculate_condition()
    print('Condition after calculation:', r1.condition)
    print(r1.check_condition(r1.condition))
