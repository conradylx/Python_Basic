# Zacznij od zaprojektowania rozgrywki
# Możliwość nazwania graczy inaczej niż X / O
# Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
# Konieczność użycia modułu random.
import random


def set_game(is_two_players):
    board = {
        1: '.', 2: '.', 3: '.',
        4: '.', 5: '.', 6: '.',
        7: '.', 8: '.', 9: '.',
    }
    end_game = False
    if is_two_players == 1:
        while end_game == False:
            print_board(board)
            set_user_input(board)
            set_comp_input(board)
            end_game = check_logic_of_game(board, is_two_players)
    else:
        while end_game == False:
            print_board(board)
            set_user_input(board)
            set_user2_input(board)
            end_game = check_logic_of_game(board, is_two_players)


def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print()


def set_user_input(board):
    user_position = int(input("Where you want to place X [choose number 1-9] "))
    while user_position > 10 or user_position < 1 or len(str(user_position)) == 2:
        user_position = int(input("Please type numbers from 1 to 9 only. Try again. "))

    if board[user_position] == '.':
        board[user_position] = 'X'

    print_board(board)


def set_user2_input(board):
    user_position = int(input("Where you want to place O [choose number 1-9] "))
    while user_position > 10 or user_position < 1:
        user_position = int(input("Please type numbers from 1 to 9 only. Try again. "))

    if board[user_position] == '.':
        board[user_position] = 'O'

    print_board(board)


def set_comp_input(board):
    pc_position = random.randrange(1, 9)

    while board[pc_position] != '.':
        pc_position = random.randrange(1, 9)

    board[pc_position] = 'O'
    print_board(board)


def check_logic_of_game(board, is_two_players):
    end_game = False
    if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
            (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
            (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or \
            (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
            (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
            (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or \
            (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or \
            (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or \
            (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        end_game = True
        print("X won")

    if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or \
            (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
            (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or \
            (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
            (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or \
            (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or \
            (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or \
            (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or \
            (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        end_game = True
        if is_two_players == 1:
            print('PC won')
        else:
            print('User2 won')

    return end_game


is_two_players = int(input("If you want to play with PC: type 1. \nIf you want to play two players game: type 2\n"))

if is_two_players > 2 or is_two_players < 1:
    print("You can only type 1 for singleplayer game and type 2 for multiplayer game.")

set_game(is_two_players)
