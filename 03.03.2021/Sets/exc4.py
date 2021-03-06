# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
#     input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#
#     output:
#
#     [4, 3, 2, 1]
#     [14, 13, 12, 11]
#     [24, 23, 22, 21]

given_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
divide_in_3 = len(given_list) // 3

list1 = list()
list2 = list()
list3 = list()

for index in range(len(given_list)):
    if index < divide_in_3:
        list1.append(given_list[index])
    if divide_in_3 <= index < divide_in_3 * 2:
        list2.append(given_list[index])
    if divide_in_3 * 2 <= index < divide_in_3 * 3:
        list3.append(given_list[index])

list1.reverse()
list2.reverse()
list3.reverse()

print('\n', list1, '\n', list2, '\n', list3)
