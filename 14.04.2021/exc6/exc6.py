# Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.


def pascal_triangle(rows):
    for line in range(1, rows + 1):
        temp = 1
        for number in range(1, line + 1):
            print(temp, ' ', end='')
            temp = int(temp * (line - number) / number)
        print()


if __name__ == '__main__':
    rows = int(input('Enter rows: '))
    pascal_triangle(rows)
