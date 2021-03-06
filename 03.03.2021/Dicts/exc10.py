# Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik,
# wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
#
# Załóżmy, że użytkownik podał N = 8
#
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

N_number = int(input("Enter range in number "))
N_dict = dict()

for index in range(1, N_number+1):
    N_dict[index] = index*index

print(N_dict)