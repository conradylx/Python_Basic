# Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika
# jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input("Enter a number "))

print("Twoja liczba jest podzielna przez 3" if number % 3 == 0 else "Nie jest podzielna")