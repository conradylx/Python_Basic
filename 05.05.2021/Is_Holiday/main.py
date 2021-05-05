import datetime
import holidays


def date_decorator(f):
    def wrapper():
        date = f()
        pl_holidays = holidays.PL()
        return pl_holidays[date] if date in pl_holidays else f"Brak święta w dniu {date}"

    return wrapper


@date_decorator
def set_date():
    date = input('Wprowadź datę w formacie DD-MM-YYYY: ')
    day, month, year = map(int, date.split('-'))
    return datetime.date(year, month, day)


if __name__ == '__main__':
    returned_day = set_date()
    print(returned_day)
