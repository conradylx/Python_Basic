# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

items = []
count = int(input("How many numbers? "))

for i in range(count):
    number = int(input("Enter number "))
    items.append(number)

if items[0] == items[-1]:
    print("Equal")
else:
    print("Not equal")
