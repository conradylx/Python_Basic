# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))
number3 = int(input("Enter third number "))
greatest = 0

'''Find largest number given'''
if number1 > number2:
    if number1 > number3:
        greatest = number1
    else:
        greatest = number3
else:
    if number2 > number3:
        greatest = number2
    else:
        greatest = number3
print("Greatest number:", greatest)

'''Find descending order of given numbers'''
if greatest == number1:
    if number3 > number2:
        print("Descending order:", number1, number3, number2)
    else:
        print("Descending order:", number1, number2, number3)
elif greatest == number2:
    if number3 > number1:
        print("Descending order:", number2, number3, number1)
    else:
        print("Descending order:", number2, number1, number3)
else:
    if number2 > number1:
        print("Descending order:", number3, number2, number1)
    else:
        print("Descending order:", number3, number1, number2)