# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
import time


def timepassed(f):
    def print_time():
        start = f()
        end = time.time()
        print('Stop')
        print(round(end - start, 5), 'sec')

    return print_time


@timepassed
def check_time_passed():
    start = time.time()
    print('Start')
    time.sleep(5)
    return start


if __name__ == '__main__':
    check_time_passed()
