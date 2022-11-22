#

from random import random, randrange


def random_list(num1, min1, max1, type1 = 'int'):       # generate list of random integer numbers
    try:
        num1 = int(num1)
        min1 = int(min1)
        max1 = int(max1)
    except ValueError:
        print('Your input was incorrect')
        exit()
    if min1 > max1:
        min1, max1 = max1, min1
    list_1 = [randrange(min1, max1) for i in range(0, num1)]
    if type1 == 'float':
        list_1 = list(map(lambda x: x + round(random(),2), list_1))  # refactor with lambda

    # if type1 == 'float':
    #     for j in range(0,num1):
    #         list_1[j] += round(random(),2)

    return list_1


def sum_list(list_2, stop2, start2=0, step2=1):    # sum numbers in a list from start to stop
    if stop2 is None:
        stop2 = len(list_2)
    for j in range(int(start2), int(stop2), int(step2)):
        sum_1 = sum(list_2[j])
    return sum_1


