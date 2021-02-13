# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
multiply = num1 * num2
divide = multiply/num3

print("Multiply:", multiply)
print("Divide:", divide)