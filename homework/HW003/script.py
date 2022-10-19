#

from random import random, randrange


def random_list(num1, min1, max1, type1 = 'int'):       # generate list of random integer numbers
    list_1 = []
    try:
        num1 = int(num1)
        min1 = int(min1)
        max1 = int(max1)
    except:
        print('Your input was incorrect')
        exit()
    if min1 > max1:
        min1, max1 = max1, min1
    list_1 = [randrange(min1, max1) for i in range(0,num1)]
    if type1 == 'float':
        for j in range(0,num1):
            list_1[j] += round(random(),2)
    return(list_1)

def sum_list(list_2, stop2, start2 = 0, step2 = 1):    # sum numbers in a list from start to stop
    sum_1 = 0
    if stop2 == None:
        stop2 = len(list_2)
    for j in range(int(start2), int(stop2), int(step2)):
        sum_1 += list_2[j]
    return sum_1

def mult_pairs_in_list(list4,show = False):
    list4_result = []
    if show:
        for i4 in range(0,(len(list4)+1)//2):
            print(list4[i4],'\t',list4[len(list4)-1-i4],'\t',list4[i4]*list4[len(list4)-1-i4])
    list4_result = [list4[i4]*list4[len(list4)-1-i4] for i4 in range(0,(len(list4)+1)//2)]
    return list4_result

def min_max_fraction(list5):
    min5 = 1
    max5 = 0
    for i5 in list5:
        min5 = min((i5 - int(i5)),min5)
        max5 = max((i5 - int(i5)),max5)
    return(round(min5,2), round(max5,2), round(max5 - min5,2))

def decimal_to_binary(num5:int):
    binary_1 = ""
    binary_2 = ""
    if num5 < 0:
        num5 = -num5
        binary_2 += "-"
    while num5 // 2 > 0:
        binary_1 += str(num5 % 2)
        num5 //= 2
    binary_1 += str(num5 % 2)
    for i6 in range(1,len(binary_1)):
        binary_2 += binary_1[-i6]
    binary_2 += binary_1[0]
    return binary_2

def nega_fibonacci(num6:int):
    list_6 = []
    list_6.append(0)
    for i in range(0,num6):
        if i == 0:
            list_6.append(1)
            list_6.insert(0,1)
        elif i == 1:
            list_6.append(1)
            list_6.insert(0,-1)
        elif i % 2 == 0:
            list_6.append(list_6[len(list_6)-1] + list_6[len(list_6)-2])
            list_6.insert(0,list_6[len(list_6)-1])
        else:
            list_6.append(list_6[len(list_6)-1] + list_6[len(list_6)-2])
            list_6.insert(0,list_6[len(list_6)-1]*(-1))
    return(list_6)