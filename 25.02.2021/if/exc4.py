# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

text = input("Enter text ")

if len(text) >= 5 and 'a' in text:
    text.replace("a", "z")
    print(text)
else:
    print("Error")