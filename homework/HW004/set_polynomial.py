# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

import script004

list_1 = script004.random_list(25, 0, 100)
#list_1 = [0, 0, 0, 1, 1]
print(list_1)
string_01 = script004.write_polynomial(list_1)
print(string_01)

file01 = open("polynomial.txt", 'a', encoding='utf8')
file01.write(string_01)
