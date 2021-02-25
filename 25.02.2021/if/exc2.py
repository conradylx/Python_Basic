# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))

sum = number1 + number2

if sum > 100:
    print(sum)
else:
    print("Koniec")