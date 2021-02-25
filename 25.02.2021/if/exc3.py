# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

rating1 = float(input("Enter 1st rating of your book "))
rating2 = float(input("Enter 2nd rating of your book "))
rating3 = float(input("Enter 3rd rating of your book "))

result = (rating1+rating2+rating3)

if result > 7:
    print("Bardzo dobry")
elif result >= 5:
    print("Przeciętna")
elif result <= 4:
    print("Nie warta uwagi")