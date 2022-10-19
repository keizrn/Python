# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import script

try:
    num_0 = (int(input('This program will show nega-Fibonacci set with N numbers before and after 0.\nPlease enter N..\n')))
except:
    print('Your input was incorrect')
    exit()

print('The nega-Fibonacci set is:')
print(script.nega_fibonacci(num_0))