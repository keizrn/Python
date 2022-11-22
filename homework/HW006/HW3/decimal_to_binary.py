#

import script


def decimal_to_binary(num5: int):  # rewritten through recursion
    if num5 >= 1:
        decimal_to_binary(num5 // 2)
        print(num5 % 2, end='')


try:
    decimal_to_binary(int(input('This program will convert your number from decimal to binary form.\nPlease input integer number..\n')))
    
except:
    print('Your input was incorrect.')
    exit()
