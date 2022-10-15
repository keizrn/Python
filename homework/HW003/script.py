#


from termcolor import colored
from random import random, randrange


def random_list(n, min, max):       # generate list of random integer numbers
    list_1 = []
    try:
        n = int(n)
        min = int(min)
        max = int(max)
    except:
        print('Your input was incorrect')
        exit()
    if min >= max:
        temp = min
        min = max
        max = temp
    for i in range(0,n):
        list_1.append(randrange(min, max))
    return(list_1)

def sum_list(list_2, stop, start = 0, step = 1):    # sum numbers in a list from start to stop
    sum_1 = 0
    if stop is None:
        stop = len(list_2)
    for j in range(int(start), int(stop), int(step)):
        sum_1 += list_2[j]
        j += step
    return sum_1

def sum_pairs_in_list(list4,show = False):
    list4_result = []
    if show:
        for i4 in range(0,len(list4)//2):
            print(list4[i4],'\t',list4[len(list4)-1-i4],'\t',colored(list4[i4]+list4[len(list4)-1-i4],'magenta'))
            list4_result.append(list4[i4]+list4[len(list4)-1-i4])
        if len(list4) % 2 > 0:
            print(list4[len(list4)//2],'\t',colored(list4[len(list4)//2]*2,'magenta'))
            list4_result.append(list4[len(list4)//2]*2)
    return list4_result


