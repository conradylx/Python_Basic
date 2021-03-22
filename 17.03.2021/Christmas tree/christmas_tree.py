"""
Utwórz funkcję rysującą choinkę według poniższego wzoru:
    *
   /|\
  /_|_\
   /|\
  / | \
 /__|__\
   /|\
  / | \
 /  |  \
/___|___\
    |
"""
def print_tree_size_2(size):
    print(" " * 6 + "*")
    center = 2
    for i in range(1, size + 1):
        if i == size:
            print(" " * (size - i + 4) + "/" + "_|" + "_" * (2 * i - size-1) + "\\")
        elif i == 1:
            print(" " * (size - i + 4) + "/" + "|" + "\\")
        else:
            print(" " * (size - i + 4) + "/" + " " * (2 * i) + "|" + " " * (i - 3) + "\\")


def print_tree_size_3(size):
    for i in range(1, size + 1):
        if i == size:
            print(" " * (size - i + 3) + "/" + "_" * (2 * i - 4) + "|" + "_" * (2 * i - size - 1) + "\\")
        elif i == 1:
            print(" " * (size - i + 3) + "/" + "|" + "\\")
        else:
            print(" " * (size - i + 3) + "/" + " " * (2 * i - 3) + "| " + " " * (i - 3) + "\\")


def print_tree_size_4(size):
    for i in range(1, size + 1):
        if i == size:
            print(" " * (size - i + 2) + "/" + "_" * (2 * i - 5) + "|" + "_" * (2 * i - size - 1) + "\\")
        elif i == 1:
            print(" " * (size - i + 2) + "/" + "|" + "\\")
        elif i == 2:
            print(" " * (size - i + 2) + "/" + " " * (2 * i - 3) + "| " + " " * (i - 4) + "\\")
        else:
            print(" " * (size - i + 2) + "/" + " " * (2 * i - 4) + "|" + " " * (i - 1) + "\\")
    print(" " * 6 + "|")


def print_tree_function():
    print_tree_size_2(2)
    print_tree_size_3(3)
    print_tree_size_4(4)


print_tree_function()

