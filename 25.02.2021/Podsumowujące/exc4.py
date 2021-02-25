# Napisz grę - kamień (k) / papier (p) / nożyce (n).
#         Użytkownik podaje jedną z 3 figur.
#         Komputer losuje jedną z 3 figur.
#         Sprawdź kto wygrał tę rundę.
#         Zmień kod tak, by użytkownik mógł podac liczbę rund.
#         Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#         Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random

rounds = int(input("Enter rounds: "))
step = 0
actions = ["r", "p", "s"]
score_user = 0
score_comp = 0

while step < rounds:
    user_figure = input("Enter figure: ").lower()
    comp_figure = random.choice(actions)

    if user_figure == "koniec":
        print("Game over!")
        break
    if user_figure not in actions:
        print("Wrong figure! Type R for Rock, P for Paper and S for Scissors!")
        continue
    if user_figure == "r" and comp_figure == "s":
        score_user += 1
        print("Player:", score_user, "Computer:", score_comp)
    elif user_figure == comp_figure:
        print("Draw!")
    elif user_figure == "p" and comp_figure == "r":
        score_user += 1
        print("Player:", score_user, "Computer:", score_comp)
    elif user_figure == "s" and comp_figure == "p":
        score_user += 1
        print("Player:", score_user, "Computer:", score_comp)
    elif user_figure == "r" and comp_figure == "p":
        score_comp += 1
        print("Player:", score_user, "Computer:", score_comp)
    elif user_figure == "p" and comp_figure == "s":
        score_comp += 1
        print("Player:", score_user, "Computer:", score_comp)
    elif user_figure == "s" and comp_figure == "r":
        score_comp += 1
        print("Player:", score_user, "Computer:", score_comp)
    else:
        print("Something went wrong")
    step += 1