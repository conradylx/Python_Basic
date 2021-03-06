# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

num_list = []

for number in range(6):
    number = int(input("Enter integer number: "))
    num_list.append(number)

center = (len(num_list)//2)-1

print(num_list)
if (num_list[center]) == num_list[center+1]:
    print("Equal")
else:
    print("Not equal")
