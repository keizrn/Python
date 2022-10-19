# Задайте строку из набора чисел. 
# Запишите ее в файл. Напишите программу, которая считает строку 
# из файла и покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# import math
# import utils

my_str = "18 12 3 14 5 6"
file_1 = open('test1.txt', 'w')
file_1.write(my_str)
file_1.close()

file_1 = open('test1.txt', 'r')
string1 = file_1.readline()
file_1.close()

my_list1 = list(map(int,string1.split()))
print(min(my_list1), max(my_list1))


# a_0,b_0,c_0 = map(int,input('Input parameters..\n').split())
# discr_0 = utils.discrim(a_0,b_0,c_0)
# x1 = (-b_0 + math.sqrt(discr_0))/(2*a_0)
# x2 = (-b_0 - math.sqrt(discr_0))/(2*a_0)
# print(x1, x2)

