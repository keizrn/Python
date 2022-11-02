import script_005

def field_draw(n_1, player_num, name_1, name_2, tic_tac_toe_array, check_win_line, winner_tag):
    header_1 = "{:3} {:1} "
    list_1 = [" ", "|"]
    separator_1 = ["---", "+"]
    for p_1 in range(0, n_1):
        header_1 += "{:3} "
        list_1.append(p_1 + 1)
        separator_1.append("---")
        header_1 += "{:1} "
        list_1.append("|")
        separator_1.append("+")
    print(header_1.format(*list_1))

    alphabet_0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for q_1 in range(0, n_1):
        print(header_1.format(*separator_1))
        list_line = [alphabet_0[q_1], "|"]
        for q_2 in range(0, n_1):
            if tic_tac_toe_array[q_1][q_2] == " X":
                list_line.append(f'\033[31m{tic_tac_toe_array[q_1][q_2]} \033[00m')
            elif tic_tac_toe_array[q_1][q_2] == " O":
                list_line.append(f'\033[32m{tic_tac_toe_array[q_1][q_2]} \033[00m')
            else:
                list_line.append(tic_tac_toe_array[q_1][q_2])
            list_line.append("|")
        print(header_1.format(*list_line))
    print(header_1.format(*separator_1))

    if winner_tag == 1:
        print(f'\033[34mPlayer {name_1} has won. Congratulations!\033[00m')
        exit()
    elif winner_tag == 2:
        print(f'Player {name_2} has won. Congratulations!')
        exit()

    if all(all(j_2 != '' for j_2 in i_2) for i_2 in tic_tac_toe_array):
        print(f'The game is over with a draw.')
        exit()

    tic_tac_toe_move(n_1, player_num, name_1, name_2, tic_tac_toe_array, check_win_line)

def tic_tac_toe_move(dimension_1, player_num, name_1, name_2, tic_tac_toe_array, check_win_line):
    alphabet_0 = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
    check_input = False
    winner_tag = ""

    while check_input == False:  # check of the input was correct
        if player_num == 1:  # user move input
            move_01 = str(input(f'\033[34mMake your move, {name_1}\n\033[00m').strip()).capitalize()
        else:
            move_01 = str(input(f'Make your move, {name_2}\n').strip()).capitalize()
        if len(move_01) == 2:
            if move_01[0].isalpha() and move_01[1].isdigit() \
                    and move_01[0] < alphabet_0[dimension_1] and int(move_01[1]) < dimension_1 + 1 \
                    and tic_tac_toe_array[alphabet_0.index(move_01[0])][int(move_01[1])-1] == '':  # check that the input was Letter + Digit and in the range
                check_input = True
            else:
                print('Your input was not correct. Please input name of the Cell in the format "A1"..')
        else:
            print('Your input was not correct. Please input name of the Cell in the format "A1"..')

    move_01_i = alphabet_0.index(move_01[0])
    move_01_j = int(move_01[1])-1

    if player_num == 1:
        string_input = " X"
    else:
        string_input = " O"

    win_line = 1
    tic_tac_toe_array[move_01_i][move_01_j] = string_input

    if move_01_i != 0:
        for count_1 in range(move_01_i - 1, -1, -1):
            if tic_tac_toe_array[count_1][move_01_j] == string_input:
                win_line += 1
            else:
                break
    if move_01_i != dimension_1 - 1:
        for count_1 in range(move_01_i + 1, dimension_1):
            if tic_tac_toe_array[count_1][move_01_j] == string_input:
                win_line += 1
            else:
                break
    if win_line < check_win_line:
        win_line = 1
        if move_01_i != 0 and move_01_j != 0:
            if move_01_i < move_01_j:
                count_2 = move_01_j - 1
                for count_1 in range(move_01_i - 1, -1, -1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_2 -= 1
                    else:
                        break
            else:
                count_1 = move_01_i - 1
                for count_2 in range(move_01_j - 1, -1, -1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_1 -= 1
                    else:
                        break

        if move_01_i != dimension_1 - 1 and move_01_j != dimension_1 - 1:
            if move_01_i > move_01_j:
                count_2 = move_01_j + 1
                for count_1 in range(move_01_i + 1, dimension_1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_2 += 1
                    else:
                        break
            else:
                count_1 = move_01_i + 1
                for count_2 in range(move_01_j + 1, dimension_1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_1 += 1
                    else:
                        break

    if win_line < check_win_line:
        win_line = 1
        if move_01_j != 0:
            for count_2 in range(move_01_j - 1, -1, -1):
                if tic_tac_toe_array[move_01_i][count_2] == string_input:
                    win_line += 1
                else:
                    break
        if move_01_j != dimension_1 - 1:
            for count_2 in range(move_01_j + 1, dimension_1):
                if tic_tac_toe_array[move_01_i][count_2] == string_input:
                    win_line += 1
                else:
                    break

    if win_line < check_win_line:
        win_line = 1
        if move_01_i != dimension_1 - 1 and move_01_j != 0:
            if (dimension_1 - move_01_i) < move_01_j:
                count_2 = move_01_j - 1
                for count_1 in range(move_01_i + 1, dimension_1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_2 -= 1
                    else:
                        break
            else:
                count_1 = move_01_i + 1
                for count_2 in range(move_01_j - 1, -1, -1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_1 += 1
                    else:
                        break

        if move_01_i != 0 and move_01_j != dimension_1 - 1:
            if move_01_i < (dimension_1 - move_01_j):
                count_2 = move_01_j + 1
                for count_1 in range(move_01_i - 1, -1, -1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_2 += 1
                    else:
                        break
            else:
                count_1 = move_01_i - 1
                for count_2 in range(move_01_j + 1, dimension_1):
                    if tic_tac_toe_array[count_1][count_2] == string_input:
                        win_line += 1
                        count_1 -= 1
                    else:
                        break

    if win_line >= check_win_line:
        winner_tag = player_num

    if player_num == 1:
        player_num = 2
    else:
        player_num = 1

    field_draw(dimension_1, player_num, name_1, name_2, tic_tac_toe_array, check_win_line, winner_tag)

try:
    dimension_1 = int(input('This is a game of Tic Tac Toe. Please input field dimension, integer (not more than 26).\n'))
except:
    print('Your input was incorrect.')
    exit()

if dimension_1 > 26:
    print('Your input was incorrect')
    exit()

name_1 = ""
while name_1 == "":
    name_1 = input('Input Name1\n')

name_2 = name_1
while name_2 == name_1 or name_2 == "":        # Check if Names are the same
    name_2 = input('Input Name2\n')     # prompt input of different name

try:
    check_win_line = int(input('Please input winning combination (3, 4, 5, etc.)\n'))
except:
    print('Your input was incorrect.')
    exit()

string_01, num_0 = script_005.flip_coin()

if num_0 == 1:
    print(f'The coin has landed on the {string_01}, so the first move is by {name_1}, who will be playing X.')
else:
    print(f'The coin has landed on the {string_01}, so the first move is by {name_2}, who will be playing X.')

tic_tac_toe_array = [['' for i_1 in range(dimension_1)] for j_1 in range(dimension_1)]

field_draw(dimension_1, 1, name_1, name_2, tic_tac_toe_array, check_win_line, "")