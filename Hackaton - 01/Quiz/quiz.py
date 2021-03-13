# Stwórz grę, która zawiera pytania z wiedzy ogólnej
import random


def random_questions(questions: dict) -> list:
    random_answer = random.choice(list(questions.items()))
    while random_answer in used_questions:
        random_answer = random.choice(list(questions.items()))
    used_questions.append(random_answer)
    return random_answer


def check_if_answer_is_correct(user_answer: str, question: list):
    if user_answer == correct_answers[question[0]]:
        print("That's correct.")
    else:
        print("That's not correct answer.")
        print(f'Correct answer is {correct_answers[question[0]]}.')


def user_answer_input() -> str:
    return input("Your answer: ")


questions = {
    1: "Gdzie urodził się M. Kopernik?",
    2: "W którym roku rozpoczęła się I wojna światowa?",
    3: "Ile lat liczy wiek?",
    4: "Kto skonstruował pierwszy telefon?",
    5: "Miasto w którym otwarto pierwsze na świecie metro?",
    6: "Gdzie znajduje się słynne Koloseum?",
    7: "Z jakiego kraju pochodził Mozart",
}

correct_answers = {
    1: "Toruń",
    2: '1914',
    3: '100',
    4: "Alexander Bell",
    5: "Londyn",
    6: "Rzym",
    7: "Austria"
}

used_questions = list()

for round in range(0, 5):
    question = random_questions(questions)
    print(question[1])
    user_answer = user_answer_input()
    check_if_answer_is_correct(user_answer, question)
