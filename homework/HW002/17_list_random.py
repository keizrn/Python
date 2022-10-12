# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

from random import random, randrange


def fill_list(num):
    new_list = []
    for i in range(-num,num+1):     # first we create a full list from -N till N
        new_list.append(i)
    temp = 0
    for j in range(0,num+1):        # then we randomly remove elements from the list
        temp = randrange(len(new_list))
        new_list.remove(new_list[temp])
    dict_rand = {}
    for k in range(0, num):
        dict_rand[k+1] = new_list[k]
    print("\n{:<8} {:<10}".format('Key','Number'))
    for p, q in dict_rand.items():
        print("{:<8} {:<10}".format(p, q))
    return dict_rand

def multiply_elements(dict1, num2):
    string1 = input(f'\nPlease input KEYS of the numbers you would like to multiply.\nSeparate them with a space.\n')
    list_int = []
    try:
        list_int = string1.split()
        n2 = len(list_int)
        result = 1
        # print(n2)
        for s1 in range(0, n2):
            list_int[s1] = int(list_int[s1])
            if ((list_int[s1] > 0) and (list_int[s1] < num2+1)):
                result *= int(dict1[list_int[s1]])
            else:
                print('Your input was incorrect.')
                return
        print(f'The result of multiplication of items {list_int} is equal to: {result}')
    except:
        print('Your input was incorrect.')

print('This program will generate array of numbers from -N till N. Amount of elements will be equal to N and will be chosen randomly.')
num1 = int(input('please input N \n'))
multiply_elements(fill_list(num1), num1)

