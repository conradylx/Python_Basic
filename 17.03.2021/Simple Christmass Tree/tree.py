def get_user_data():
    sign = input("Enter sign to build your tree: ")
    while sign.isalpha() or sign.isdigit() or sign == ' ' or len(sign) > 1:
        sign = input("Typed letter or number or two characters. Allowed only special signs. Try again: ")
    size = int(input("Enter size of the tree: "))
    return sign, size


def print_tree(sign: str, size: int):
    for i in range(0, size + 1):
        print(" " * (size - i) + sign * (2 * i) + sign)
    print(" " * ((size)) + "|")


sign, size = get_user_data()
print_tree(sign, size)
