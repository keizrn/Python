#


from random import random, randrange


def random_list(num1, min1, max1):
    try:
        num1 = int(num1)
        min1 = int(min1)
        max1 = int(max1)
    except:
        print('Your input was incorrect.')
        exit()
    list_1 = [randrange(min1, max1+1) for i1 in range(0, num1)]
    return(list_1)


def list_to_dict(list_2):
    dict_2 = {}
    for i2 in list_2:
        if dict_2.get(i2) is None:
            dict_2[i2] = 1
        else:
            dict_2[i2] += 1
    return dict_2

def print_dict_by_columns(dict_3):
     print("Number".ljust(10), "Times")
     for i3 in dict_3:
         print(str(i3).ljust(10), dict_3[i3])

def nonrecurr_dict(dict_4):
    list_4 = []
    for i4 in dict_4:
        if dict_4[i4] == 1:
            list_4.append(i4)
    return(list_4)

def find_simple_numbers(num_5):
    list_5 = list(range(num_5))
    for i5 in range(0, len(list_5)):
        for i5_a in range(i5+1, len(list_5)):
            if list_5[i5_a] % list_5[i5] == 0:
                list_5.remove(i5_a)
    print(list_5)

def write_polynomial(list_02):
    string_02 = ""
    sup_02 = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    if all(item_02 == 0 for item_02 in list_02):
        string_02 += "0"
    else:
        k_02 = len(list_02) - 1
        for i_02 in range(0, len(list_02)):
            if list_02[i_02] == 0:
                k_02 -= 1
                continue
            if i_02 == 0:
                if list_02[i_02] > 1 or list_02[i_02] < 0:
                    string_02 += str(list_02[i_02])
            elif list_02[i_02] < 0:
                string_02 += str(list_02[i_02])
            elif list_02[i_02] > 0:
                if string_02 != "":
                    string_02 += "+ "
                if list_02[i_02] != 1 or i_02 == len(list_02)-1:
                    string_02 += str(list_02[i_02])

            if i_02 == len(list_02)-2:
                string_02 += "x "
            elif i_02 == len(list_02) - 1:
                string_02 += " "
            else:
                string_02 += "x" + str(k_02).translate(sup_02) + " "
            k_02 -= 1
        string_02 += "= 0"
    return string_02

def read_polynomial(string_06):
    dict_06 = {}
    string_06 = string_06.replace(" = 0", "x⁰")
    list_06 = string_06.split(" + ")
    anti_sup_02 = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    for item_06 in range(len(list_06)):
        list_06[item_06] = list_06[item_06].split('x')
        if list_06[item_06][0] == "":
            list_06[item_06][0] = 1
        if list_06[item_06][1] == "":
            list_06[item_06][1] = "1"
        list_06[item_06][1] = list_06[item_06][1].translate(anti_sup_02)
        dict_06[int(list_06[item_06][1])] = int(list_06[item_06][0])
    return dict_06

def merge_dicts(dict_001, dict_002):
    dict_sum = {}
    for i_07 in dict_001:
        if i_07 not in dict_002:
            dict_sum[i_07] = dict_001[i_07]
        else:
            dict_sum[i_07] = dict_001[i_07] + dict_002[i_07]
    for j_07 in dict_002:
        if j_07 not in dict_sum:
            dict_sum[j_07] = dict_002[j_07]
    return dict_sum

def dict_to_list(dict_07):
    list_07 = []
    i_07 = max(dict_07)
    while i_07 >= 0:
        if i_07 not in dict_07:
            list_07.append(0)
        else:
            list_07.append(dict_07.pop(i_07))
        i_07 -= 1
    return list_07