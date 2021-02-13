# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
divide = num1//num2
rest = num1%num2

print("Divide:", divide)
print("Rest:",rest)