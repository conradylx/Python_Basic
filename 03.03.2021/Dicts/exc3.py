# Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

# n = 3
#
# tab = [
#     ['-', '-', '-'],
#     ['-', '-', '-'],
#     ['-', '-', '-']
# ]
#
# for i in range(n):
#     print(' '.join(tab[i]))

size = int(input("Enter size of the array "))
tab = [['-'] * size] * size

for row in tab:
    print(' '.join(row))