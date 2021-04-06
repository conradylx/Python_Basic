# Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz
# jej długość np.
# Wejście:
#     var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście
#     ‘nnnnnnnnn’, 9
#     Utwórz generator instancji testowych, który wygeneruje losowe
#     ciągi znaków składające się z jedynie z cyfr od 0-9.
#         Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
#     Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika
#         np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
#     Zaimportuj generator bezpośrednio do programu.

from sequences_file import check_longest_sequence
from sequence_generator import generate_numeric_string

if __name__ == '__main__':
    user_text = input("Enter text sequence: ")
    max_seq_string, string_len = check_longest_sequence(user_text)
    print(max_seq_string, string_len)

    generated_string = generate_numeric_string(user_text)
    print(generated_string)

    max_seq_string, string_len = check_longest_sequence(generated_string)
    print(max_seq_string, string_len)
