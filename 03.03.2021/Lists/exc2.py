# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

numbers = []

for number in range(10):
    user_input = int(input("Enter your number "))
    if user_input % 2 == 0:
        numbers.append(user_input)

print(numbers)
