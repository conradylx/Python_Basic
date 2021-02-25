"""
Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i
zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
"""
text = "abrakadabra"
text_length = len(text)//2
print(text[text_length-1:text_length+2:1])

""" Do zmiennej quote przypisz zdanie:
    „Honesty is the first chapter in the book of wisdom.”, a następnie:
    Policz wszystkie znaki w napisie
    Nie modyfikując zmiennej wyświetl słowo wisdom
    Wyświetl tylko pierwszą połowę tekstu
    Wyświetl tylko kropkę
    Wyświetl od połowy tylko co trzecią literę cytatu
    Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
    Wyświetl cały cytat odwrotnie
    Zamień wisdom na słowo friendship
"""

quote = 'Honesty is the first chapter in the book of wisdom.'
print(len(quote))
print(quote[-7: -1 :1])
half_len = len(quote)//2
print(quote[0:half_len:1])
print(quote[-1])
print(quote[half_len::3])
print(quote[::3])
print(quote[::-1])
print(quote.replace("wisdom", "friendship"))
