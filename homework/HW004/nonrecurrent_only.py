# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

import script004


print('This program will generate the random list of integers and then show you only strictly non-recurrent elements.')
num_0, min_0, max_0 = map(int,input('Please input Number of elements, min & max of the random range, split with space.\n').split())
list_01 = (script004.random_list(num_0, min_0, max_0))
print('Initial list is:\n',list_01,'\n')
dict_01 = (script004.list_to_dict(list_01))
script004.print_dict_by_columns(dict_01)

print('\nStrictly unique elements are:')
print(script004.nonrecurr_dict(dict_01))
