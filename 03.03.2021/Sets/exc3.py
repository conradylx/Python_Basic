# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (33, 44, 55, 66, 77)

list1 = list(my_tuple1[::2])
list2 = list(my_tuple2[1::2])

all_lists = list1 + list2
my_set = set(all_lists)
print(my_set)
