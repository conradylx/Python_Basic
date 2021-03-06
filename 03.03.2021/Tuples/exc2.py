# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

my_tuple = ('A', 'B', 'C', 'A', 'B', 'B')

for index in my_tuple:
    if my_tuple.count(index) > 1:
        print(index)