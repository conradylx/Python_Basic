# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
import time


def timepassed(f):
    def print_time():
        start = f()
        end = time.time()
        print(end - start)

    return print_time


@timepassed
def check_time_passed():
    start = time.time()
    print('Hello')
    return start


if __name__ == '__main__':
    check_time_passed()
