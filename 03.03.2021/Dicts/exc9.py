# Użytkowników poproś o podanie 4 przedmiotów szkolnych,
# sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
from collections import Counter

user_count = int(input("How many users? "))
number_of_subjects = 4
subjects = []

for user in range(1, user_count + 1):
    inside_list = []
    for subject in range(1, number_of_subjects + 1):
        inside_list.append(input("Enter a subject ").lower().capitalize())
    subjects.append(tuple(inside_list))

print(subjects)

words_counter = Counter()
is_repeated = False

for lists in subjects:
    for word in set(lists):
        words_counter[word] += 1
        is_repeated = True

if is_repeated:
    print("There are repeated subjects")
    print(f'{max(words_counter.keys())} is the most popular subject')
else:
    print("There is no repeated subjects")
