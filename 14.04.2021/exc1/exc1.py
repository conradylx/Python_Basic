# Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.

def euclid_nwd(a, b):
    result = a % b
    if a % b != 0:
        a = b
        b = result
        return euclid_nwd(a, b)
    else:
        return b


if __name__ == '__main__':
    a = 282
    b = 78
    result = euclid_nwd(a, b)
    print(f'NWD of {a} and {b} is {result}')
