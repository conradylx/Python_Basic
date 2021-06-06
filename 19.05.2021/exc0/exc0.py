def triangle(a, h):
    validate_args(a, h)
    return (a * h) * 0.5


def trapezoid(a, b, h):
    validate_args(a, b, h)
    return ((a + b) * 0.5) * h


def validate_args(*values: list):
    for arg in values:
        if not isinstance(arg, (int, float)):
            raise TypeError(f'Bok musi być wartością liczbową, a jest \'{type(arg).__name__}\'')


if __name__ == '__main__':
    print(trapezoid(2, '4', 5))
