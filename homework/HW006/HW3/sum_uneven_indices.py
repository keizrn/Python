# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import script


def print_uneven_color(list_3):         
    for l in range(0, len(list_3)//2):
        print(list_3[l*2], '\t', list_3[l*2+1])
    if len(list_3) % 2 > 0:
        print(list_3[len(list_3)-1])

list1 = script.random_list(
    input("This program will calculate sum of integers with uneven indices.\nLet's fill in a list with random numbers.\nPlease input a number of elements in the list..\n"), 
    input("Now please input minimal number for random generation..\n"), 
    input("And a maximal number..\n"))
print(f'The random list is: {list1}')
print('Now, the same list split into 2 columns:')
print_uneven_color(list1)
print(f'The sum of numbers with uneven indices is: ', script.sum_list(list1, len(list1), 1, 2))