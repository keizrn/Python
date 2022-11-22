#

import script


def mult_pairs_in_list(list4, show=False):
    if show:
        for i4 in range(0, (len(list4)+1)//2):
            print(list4[i4], '\t',
                  list4[len(list4)-1-i4], '\t',
                  list4[i4]*list4[len(list4)-1-i4])

    list4_result = [list4[i4]*list4[len(list4)-1-i4] for i4 in range(0, (len(list4)+1)//2)]
    return list4_result


list1 = script.random_list(input("This program will multiply pairs of numbers in the random list. 1st with the last, 2nd & 2nd to last, etc.\nNow please indicate a size of the list..\n"),
                           input('Please indicate minimal number for random generation..\n'),
                           input('And a maximal border..\n'))
print('The random list is:', list1)
print('The result is:', mult_pairs_in_list(list1, True))
