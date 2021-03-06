# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
#
# >>>  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

list_to_tuple = tuple(set(example_list))
min_value = min(list_to_tuple)
max_value = max(list_to_tuple)
print(list_to_tuple, min_value, max_value)
