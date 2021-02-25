# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Enter password ")

if len(password) >= 8 and not password.islower() and not password.isalpha():
    print("Password is correct")
else:
    print("Password is not correct")

# print("Password is correct" if len(password) >= 8 \
# and not password.islower() and not password.isalpha() else "Password is not correct")
