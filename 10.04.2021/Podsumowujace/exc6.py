# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
import random


def get_round() -> tuple:
    score_user, score_comp = 0, 0
    actions = ["r", "p", "s"]

    user_figure = input("Enter figure: ").lower()
    comp_figure = random.choice(actions)

    if user_figure == "koniec":
        print("Game over!")

    if user_figure not in actions:
        print("Wrong figure! Type R for Rock, P for Paper and S for Scissors!")

    if (user_figure == "r" and comp_figure == "s") or (user_figure == "p" and comp_figure == "r")\
            or (user_figure == "s" and comp_figure == "p"):
        score_user += 1
        print("User win")
    elif (user_figure == "r" and comp_figure == "p") or (user_figure == "p" and comp_figure == "s")\
            or (user_figure == "s" and comp_figure == "r"):
        score_comp += 1
        print("Computer win")
    elif user_figure == comp_figure:
        print("Draw!")
    else:
        print("Something went wrong")

    return score_comp, score_user


def show_score(score_comp, score_user):
    print(f'Your score: {score_user}, Computer score: {score_comp}')


def start_game():
    score_comp, score_user = 0, 0
    for i in range(3):
        score_comp_temp, score_user_temp = get_round()
        if score_comp_temp == 1:
            score_comp += 1
        elif score_user_temp == 1:
            score_user += 1

    show_score(score_comp, score_user)


start_game()
