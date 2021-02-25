# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

given_number = int(input("Enter your number "))
guess_number = 25

if guess_number == given_number:
    print("Correct!")
else:
    print("Incorrect!")