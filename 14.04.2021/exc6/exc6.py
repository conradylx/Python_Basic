# Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.

def find_factorial(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * find_factorial(i - 1)


def find_rows(n, k):
    return int(find_factorial(n)/(find_factorial(n-k)*find_factorial(k)))


def pascal_triangle(rows):
    for n in range(0, rows):
        for k in range(0, n + 1):
            print(find_rows(n, k), " ", end="")
        print()


if __name__ == '__main__':
    rows = int(input('Enter rows: '))
    pascal_triangle(rows)
