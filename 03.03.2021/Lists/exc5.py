# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#     Dorota, Wellman, dziennikarka
#     Adam, Małysz, sportowiec
#     Robert, Lewandowski, piłkarz
#     Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

TwoDimArray = [
    ['Dorota', 'Wellman', 'Dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka'],
]

for row in TwoDimArray:
    print(', '.join(row))

# for row in TwoDimArray:
#     for col in row:
#         print(col, end=" ")
#     print()
