# Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def find_max_len_word(text: str) -> str:
    try:
        with open(text, encoding='UTF-8', mode='r') as file:
            data = file.read()\
                .replace(',', '')\
                .replace('.', '')\
                .replace(';', '')\
                .split()

            max_word = ""
            for word in data:
                if len(word) > len(max_word):
                    max_word = word
    except FileNotFoundError:
        print(f"File {text} not found.")
    return max_word


print(find_max_len_word('text.txt'))
