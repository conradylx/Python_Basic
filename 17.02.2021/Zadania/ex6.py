"""
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book
"""
title = input("Enter book's title ")
author = input("Enter author's name ")
pages = input("Enter pages count ")

print(title.isalpha())
print(author.isalpha())
print(pages.isdigit())
book = title.capitalize() + ", " + author.capitalize() + " and has pages: " + pages
print(book)

