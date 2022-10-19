#

import script

try:
    print(f'Result binary number is:',
        script.decimal_to_binary(int(input('This program will convert your number from decimal to binary form.\nPlease input integer number..\n'))))
    
except:
    print('Your input was incorrect.')
    exit()