# Wyświetl 3 losowe cytaty

import random

try:
    with open('text.txt', 'r', encoding='UTF-8') as file:
        lines = list(file)
        for line in range(3):
            random_line = random.choice(lines)
            print(random_line)

except FileNotFoundError:
    print("File not found")
