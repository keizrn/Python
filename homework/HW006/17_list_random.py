# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

from random import random, randrange
from typing import List


def fill_list(num):
    new_list = [i for i in range(-num, num+1)]  # first we create a full list from -N till N - упростила наполнение генератором
    for j in range(0, num + 1):  # then we randomly remove elements from the list
        new_list.remove(new_list[randrange(len(new_list))])  # упростила удаление случайным образом
    dict_rand = dict(zip(range(1, num+1), new_list))
    print("\n{:<8} {:<10}".format('Key', 'Number'))
    for p, q in dict_rand.items():
        print("{:<8} {:<10}".format(p, q))
    return dict_rand

def multiply_elements(dict1, num2):
    string1 = input(f'\nPlease input KEYS of the numbers you would like to multiply.\nSeparate them with a space.\n')
    try:
        result_1 = 1
        list_int = list(map(int, string1.split()))
        for key, value in dict1.items():    # значительно упростила работу со словарем
            if key in list_int:
                result_1 *= value
        print(f'The result of multiplication of items {list_int} is equal to: {result_1}')
    except:
        print('Your input was incorrect.')

print('This program will generate array of numbers from -N till N. Amount of elements will be equal to N and will be chosen randomly.')
num1 = int(input('please input N \n'))
multiply_elements(fill_list(num1), num1)

