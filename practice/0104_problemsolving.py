# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

# num1 = int(input('Введите число 1.. '))
# num2 = int(input('Введите число 2.. '))
# if num1*num1 == num2 or num2*num2 == num1:
#     max = max(num1,num2)
#     min = min(num1,num2)
#     print(f'Да, число {max} является квадратом числа {min}')
# else:
#     print('no squares')



#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# my_list = [int(input('Input 5 numbers \n')),int(input()),int(input()),int(input()),int(input())]
# max = my_list[0]
# for i in my_list:
#     if i > max:
#         max = i
# print(f'Maximum element is {max}')


# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('Введите N.. '))
# if N < 0:
#     N = -N
# s = ''
# for i in range(-N, N+1, 1):
#     s += str(i)
#     s += ' '
# print(s)

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# num = float(input('Input number.. '))
# num10 = num * 10
# result = int(num10 % 10)
# print(result)

# Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Input number to check..'))
if ((num % 5 == 0 and num % 10 == 0) or (num % 15 == 0)) and (num % 30 != 0):
    print('Number OK')
else:
    print('Number not OK')
