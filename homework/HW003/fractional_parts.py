# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import script

list1 = script.random_list(
    input("This program will calculate difference between min & max fractions of random real numbers in a list.\nLet's start with a list.\nPlease input a number of elements in the list..\n"), 
    input("Now please input minimal number for random generation..\n"), 
    input("And a maximal number..\n"), 'float')
print(f'The random list is: {list1}')
min1, max1, diff1 = script.min_max_fraction(list1)
print(f'{max1} - {min1} = {diff1}')