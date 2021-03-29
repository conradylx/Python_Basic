# Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji.
# Dane wejściowe pobierz z pliku csv (plik csv możesz traktować jako plik txt ze znanym znakiem podziału),
# który będzie przechowywał dane potrzebne do generowania.
import csv
import random


def read_file() -> dict:
    reader_dict = dict()
    with open('quotes.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        iterator = 0
        for line in reader:
            value, key = line[0], line[1]
            reader_dict[key] = f'"{value}"'
            iterator += 1
    return reader_dict


def get_random_quote(quotes: dict):
    random_quote = random.choice(list(quotes.values()))
    for author, quote in quotes.items():
        if quote == random_quote:
            print(random_quote, author)


reader_dict = read_file()
get_random_quote(reader_dict)
