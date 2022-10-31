#
from random import randrange

import script_005

def candy_bot(diff_1, remain_q):
    rand_0 = randrange(0, 100)  # % of mistake
    if diff_1 == 1:  # easy difficulty
        round_1 = 0.7  # deviation from correct answer
        rand_mistake = 60  # chance of mistake
    elif diff_1 == 2:  # medium
        round_1 = 0.8
        rand_mistake = 40
    else:  # hard
        round_1 = 0.9
        rand_mistake = 10

    if rand_0 < rand_mistake:  # if mistake to be done
        move_new = max(int((remain_q % 29) * round_1), 1)
    else:  # if no mistake
        move_new = max(remain_q % 29, 1)

    print(f'Bot has picked {move_new} candies')
    return move_new

def candy_game_move(player_num, name_1, name_2, remain_q, initial_q, diff_level):  # MAIN GAME FUNCTION
    if player_num == 1:  # user move input
        move_01 = input(f'\033[36m{remain_q} candies remaining. Make your move, {name_1}\n\033[00m')
    else:
        if name_2 == "\033[00mBot":
            move_01 = candy_bot(diff_level, remain_q)
        else:
            move_01 = input(f'{remain_q} candies remaining. Make your move, {name_2}\n')

    try:
        move_01 = int(move_01)
    except:  # check if not integer input
        print('\033[31mYour input was incorrect! Please repeat.\033[00m')
        candy_game_move(player_num, name_1, name_2, remain_q, initial_q, diff_level)  # prompt move one more time
    if move_01 < 1 or move_01 > remain_q or move_01 > 28:  # check if not correct number input
        print('\033[31mYour input was incorrect! Please repeat.\033[00m')
        candy_game_move(player_num, name_1, name_2, remain_q, initial_q, diff_level)

    remain_q -= move_01  # main move

    if remain_q == 0:  # check if WIN (end of game)
        if player_num == 1:
            print(f'\033[36mPlayer {name_1} has won and gets all {initial_q} candies. Congratulations, \033[01m{name_1}!\033[00m')
            exit()
        else:
            print(f'Player {name_2} has won and gets all {initial_q} candies. Congratulations, \033[01m{name_2}!\033[00m')
            exit()
    else:
        if player_num == 1:     # change player section
            player_num = 2
        else:
            player_num = 1

        candy_game_move(player_num, name_1, name_2, remain_q, initial_q, diff_level)   # main recursion

def candies_number():       # Cycle to choose number of candies
    try:
        q_0 = int(input('Please input initial number of candies..\n'))
    except:
        print('Your input was incorrect.')
        q_0 = candies_number()
    if q_0 > 28:
        return q_0
    else:
        print('Your input was incorrect.')
        exit()

def game_choice():      # Cycle to choose 2 player mode or bot game
    try:
        g_0 = int(input('Please choose game mode: 1 - Two Players OR 2 - Player vs Bot..\n'))
    except:
        print('Please choose again. Either 1 or 2.')
        g_0 = game_choice()
    if g_0 == 1 or g_0 == 2:
        return g_0
    else:
        print('Please choose again. Either 1 or 2.')
        exit()

def diff_choice():
    try:
        diff_0 = int(input('Please choose difficulty of the Bot: 1 - Easy, 2 - Medium, 3 - Hard..\n'))
    except:
        print('Please choose again. Either 1, 2 or 3')
        diff_0 = diff_choice()
    if diff_0 == 1 or diff_0 == 2 or diff_0 == 3:
        return diff_0
    else:
        print('Please choose again. Either 1, 2 or 3')
        exit()


print('This is a 2 players candy game. Each player takes not more than 28 candies.\nPlease note that the player who makes the LAST move WINS and takes all the candies.\n')
initial_q = candies_number()
game_choice = game_choice()
if game_choice == 2:
    diff_level = diff_choice()
else:
    diff_level = 0
name_1 = ""
while name_1 == "":
    name_1 = input('\033[36mInput Name1\n\033[00m')
if game_choice == 1:
    name_2 = name_1
    while name_2 == name_1 or name_2 == "":        # Check if Names are the same
        name_2 = input('Input Name2\n')     # prompt input of different name
else:
    name_2 = "\033[00mBot"
string_01, num_0 = script_005.flip_coin()
if num_0 == 1:
    print(f'The coin has landed on the {string_01}, so the first move is by {name_1}.')
else:
    print(f'The coin has landed on the {string_01}, so the first move is by {name_2}.')
candy_game_move(num_0, name_1, name_2, initial_q, initial_q, diff_level)