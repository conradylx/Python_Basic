# Customer <-- ma pola imię nazwisko, oraz email
# oraz metodę rejestracji, która zwraca datę o tyle dni do przodu ile customer ma liter w imieniu i nazwisku

import datetime
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    surname: str
    email: str

    def register(self):
        count_chars = len(self.name) + len(self.surname)
        date = datetime.today()
        end_date = date + timedelta(count_chars)
        print(end_date.strftime('%d/%m/%Y'))


if __name__ == '__main__':
    c1 = Customer('John', 'Doe', 'jdoe@mail.com')
    c1.register()
