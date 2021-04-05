def calculate_delta(a: int, b: int, c: int) -> int:
    """
    Function calculates delta from given arguments.
    """
    return (pow(b, 2) - (4 * a * c))


if __name__ == '__main__':
    print(calculate_delta(3, 5, 2))
