def check_longest_sequence(text: str) -> tuple:
    text = text.lower()
    max_len = 1
    actual_len = 1
    prev_char = None
    max_rep_word = []

    for char in text:
        if char == prev_char:
            actual_len += 1
            if actual_len > max_len:
                max_rep_word.clear()
                max_rep_word.append(char)
            max_len = max(max_len, actual_len)
        else:
            actual_len = 1

        prev_char = char

    return "".join(max_rep_word * max_len), max_len


if __name__ == '__main__':
    print(check_longest_sequence('banannnnannnnnnnnnanananananaaaana'))
