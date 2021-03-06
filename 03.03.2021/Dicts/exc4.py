# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

multiplication_list = []
list_size = 10

'''
Generate multiplication table.
list_size is increased by 1, because 0 in table is omitted.
'''
for row in range(1, list_size+1):
    temp = []
    for col in range(1, list_size+1):
        temp.append(row*col)
    multiplication_list.append(temp)

'''
Print table. Used string formatting.
'''
for number in multiplication_list:
    print("{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}".format(*number))
