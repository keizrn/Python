#

import script

list1 = script.random_list(input("This program will sum pairs of numbers in the random list. 1st with the last, 2nd & 2nd to last, etc.\nNow please indicate a size of the list..\n"),
                            input('Please indicate minimal number for random generation..\n'),
                            input('And a maximal border..\n'))
print('The random list is:',list1)
print('The result is:',script.mult_pairs_in_list(list1,True))