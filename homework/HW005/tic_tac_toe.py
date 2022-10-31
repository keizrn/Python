import script_005

def field_draw(n_1, player_num, name_1, name_2, tic_tac_toe_array):
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

    alphabet_0 = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
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

    if player_num == 1:
        player_num = 2
    else:
        player_num = 1

    tic_tac_toe_move(n_1, player_num, name_1, name_2, tic_tac_toe_array)

def tic_tac_toe_move(dimension_1, player_num, name_1, name_2, tic_tac_toe_array):
    alphabet_0 = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
    check_input = False
    while check_input == False:  # check of the input was correct
        if player_num == 1:  # user move input
            move_01 = str(input(f'\033[36mMake your move, {name_1}\n\033[00m').strip()).capitalize()
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
        if tic_tac_toe_array[move_01_i-1][move_01_j] == string_input:
            win_line += 1
            if move_01_i-1 != 0:
                if tic_tac_toe_array[move_01_i - 2][move_01_j] == string_input:
                    win_line += 1
            elif move_01_i != dimension_1-1:
                if tic_tac_toe_array[move_01_i + 1][move_01_j] == string_input:
                    win_line += 1
    print(win_line)



    field_draw(dimension_1, player_num, name_1, name_2, tic_tac_toe_array)








# dimension_1 = int(input('This is a game of Tic Tac Toe. Please input field dimensions.\n'))
# name_1 = ""
# while name_1 == "":
#     name_1 = input('\033[34mInput Name1\n\033[00m')
# #if game_choice == 1:
# name_2 = name_1
# while name_2 == name_1 or name_2 == "":        # Check if Names are the same
#     name_2 = input('Input Name2\n')     # prompt input of different name
# #else:
# #    name_2 = "\033[00mBot"
# string_01, num_0 = script_005.flip_coin()
# if num_0 == 1:
#     print(f'The coin has landed on the {string_01}, so the first move is by {name_1}, who will be playing X.')
# else:
#     print(f'The coin has landed on the {string_01}, so the first move is by {name_2}, who will be playing X.')
dimension_1 = 5
name_1 = "Nata"
name_2 = "Lena"
player_num = 1
tic_tac_toe_array = [['' for i_1 in range(dimension_1)] for j_1 in range(dimension_1)]
field_draw(dimension_1, player_num, name_1, name_2, tic_tac_toe_array)