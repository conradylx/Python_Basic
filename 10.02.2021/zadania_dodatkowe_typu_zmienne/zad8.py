# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

amount = float(input("Enter amount of cash to withdraw "))
euro = int(amount/4.20)
dollar = int(amount/4.60)

fifty = dollar // 50
twenty = dollar % 50 // 20
ten = dollar % 50 % 20 // 10
five = dollar % 50 % 20 % 10 // 5
two = dollar % 50 % 20 % 10 % 5 // 2
one = dollar % 50 % 20 % 10 % 5 % 2 //1

fiftyEUR = euro // 50
twentyEUR = euro % 50 // 20
tenEUR = euro % 50 % 20 // 10
fiveEUR = euro % 50 % 20 % 10 // 5
twoEUR = euro % 50 % 20 % 10 % 5 // 2
oneEUR = euro % 50 % 20 % 10 % 5 % 2 //1

print("-------------------------------------------------------------------------------------------")
print("Amount converted to euro is {0} EUR and converted to dollars {1} USD".format(euro, dollar))
print("-------------------------------------------------------------------------------------------")
print("You'll get these notes in USD: 50: {0}, 20: {1}, 10: {2}, 5: {3}, 2: {4}, 1: {5}".format(fifty, twenty, ten, five, two, one))
print("You'll get these notes in EUR: 50: {0}, 20: {1}, 10: {2}, 5: {3}, 2: {4}, 1: {5}".format(fiftyEUR, twentyEUR, tenEUR, fiveEUR, twoEUR, oneEUR))
print("-------------------------------------------------------------------------------------------")
