# Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

some_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

usr_input = int(input("Please enter a number: "))

print(some_tuple.index(usr_input)) if usr_input in some_tuple else print("Not found")
