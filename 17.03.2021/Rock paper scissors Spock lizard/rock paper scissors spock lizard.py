# # Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
# Po każdej rundzie zapytajmy użytkownika, czy chce kontynuować grę:
# Would you like to continue yes/no:
# Komputer może być także uparty. Jeśli użytkownik nie zadecyduje w poprzednim kroku, zadaj pytanie dodatkowe:
# No!? We had so much fun together! You will not get away so easily! Prepare yourself for the next round!

#Update2: Added Spock and Lizard values.

import random


def welcome_user():
    print('Welcome!\n S - start game\n P - difficulty level\n Q - quit')
    user_start_decision = input("Type your decision: ").capitalize()

    while user_start_decision != 'S' and user_start_decision != 'P' and user_start_decision != 'Q':
        user_start_decision = input("Type valid decision: ").capitalize()

    if user_start_decision == 'S':
        start_game(1)
    elif user_start_decision == 'P':
        difficulty = get_level_difficulty()
        start_game(difficulty)
    elif user_start_decision == 'Q':
        quit()


def get_round(difficulty: int) -> tuple:
    score_user, score_comp = 0, 0
    actions = ["r", "p", "s", "spock", "liz"]

    user_figure = input("Enter figure: ").lower()
    if difficulty == 1:
        comp_figure = random.choice(actions)
    else:
        for level in range(3):
            actions.append(user_figure)
        comp_figure = random.choice(actions)

    if user_figure == "koniec":
        print("Game over!")
    print(comp_figure)
    if user_figure not in actions:
        print("Wrong figure! Type R for Rock, P for Paper, S for Scissors, Spock for Spock and Liz for Lizard!")

    if (user_figure == "r" and comp_figure == "s") or (user_figure == "p" and comp_figure == "r") \
            or (user_figure == "s" and comp_figure == "p") or (user_figure == "spock" and
                (comp_figure == "r" or comp_figure == "s")) or (user_figure == "p" and comp_figure == "spock") or \
                (user_figure == "liz" and (comp_figure == "spock" or comp_figure == "p")) or \
                ((user_figure == "r" or user_figure == "s") and comp_figure == "liz"):
        score_user += 1
        print("User win")
    elif (user_figure == "r" and comp_figure == "p") or (user_figure == "p" and comp_figure == "s") \
            or (user_figure == "s" and comp_figure == "r") or (user_figure == "spock" and
                comp_figure == "p") or (user_figure == "r" and comp_figure == "spock") or \
                (user_figure == "s" and comp_figure == "spock") or \
                (user_figure == "liz" and (comp_figure == "s" or comp_figure == "r")) or \
                (user_figure == "p" and comp_figure == "liz") or (user_figure == "spock" and comp_figure == "liz"):
        score_comp += 1
        print("Computer win")
    elif user_figure == comp_figure:
        print("Draw!")
    else:
        print("Something went wrong")

    if difficulty == 2:
        for level in range(3):
            actions.pop()
    return score_comp, score_user


def show_score(score_comp: int, score_user: int, rounds: int):
    print(f'Your score: {score_user}, Computer score: {score_comp}')
    print(f'You did {rounds} rounds and your victory is in {int((score_user/rounds)*100)}%!')


def get_level_difficulty() -> int:
    print(" Difficulty levels:\n 1 - novice\n 2 - pro\n")
    get_lvl = int(input("Type your level: "))
    while get_lvl != 1 and get_lvl != 2:
        get_lvl = int(input("Type correct level: "))
    return get_lvl


def start_game(difficulty: int):
    print('Decisions:\n R - rock\n P - paper\n S - Scissors\n Spock - Spock\n Liz = Lizard\n')
    score_comp, score_user = 0, 0
    decision = True
    rounds = 1
    while decision:
        score_comp_temp, score_user_temp = get_round(difficulty)
        if score_comp_temp == 1:
            score_comp += 1
        elif score_user_temp == 1:
            score_user += 1
        decision = ask_if_continue()
        rounds += 1
    show_score(score_comp, score_user, rounds)


def ask_if_continue() -> bool:
    ask_decision = input("Would you like to continue? Type: Yes or No ").capitalize()
    decision = False

    while ask_decision != 'Yes' and ask_decision != 'No':
        ask_decision = input("Wrong decision. Type: Yes or No ").capitalize()

    if ask_decision == 'Yes':
        return True
    elif ask_decision == 'No':
        decision = bool(random.getrandbits(1))
        if decision:
            print(
                'No!? We had so much fun together! You will not get away so easily! Prepare yourself for the next round!')

    return decision


welcome_user()
