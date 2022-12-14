# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

import script004

list_1 = script004.random_list(15, 0, 10)
string_01 = script004.write_polynomial(list_1)

file01 = open("polynomial2.txt", 'w', encoding='utf8')  # save 1st polynomial to file
file01.write(string_01)
file01.close()

list_1 = script004.random_list(15, 0, 10)
string_01 = script004.write_polynomial(list_1)

file01 = open("polynomial3.txt", 'w', encoding='utf8')  # save 2nd polynomial to file
file01.write(string_01)
file01.close()

file_1 = open('polynomial2.txt', 'r', encoding='utf-8')
file_2 = open('polynomial3.txt', 'r', encoding='utf-8')

string_01 = file_1.readline()
print(string_01)
string_02 = file_2.readline()
print(string_02)

dict_01 = script004.read_polynomial(string_01)  # dictionary of coeff from 1st polynomial
dict_02 = script004.read_polynomial(string_02)  # dictionary of coeff from 2nd polynomial
dict_sum = script004.merge_dicts(dict_01, dict_02)  # dictionary of coeff from result polynomial

list_sum = script004.dict_to_list((dict_sum))   # list of coefficient of result polynom - ready for file writing

string_sum = script004.write_polynomial(list_sum)
print(f'Result polynomial:')
print(string_sum)

file01 = open("polynomial_sum.txt", 'w', encoding='utf8')  # write result polynomial into file
file01.write(string_sum)
file01.close()

file_1.close()
file_2.close()