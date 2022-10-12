# Выяснить, является ли число кратным заданному, если нет, вывести остаток



# Показать последнюю цифру 3-значного числа


# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

# N = int(input('Input N.. \n'))
# out = 1
# list_3 = [out]
# for i in range(0,N-1):
#     out *= -3
#     list_3.append(out)
# print(list_3)


# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('input number \n'))
# dict_1 = {}
# for i in range(0,n):
#     dict_1[i] = 3*i + 1
# print(dict_1)


# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = input('input 1st string\n')
str2 = input('input 2nd string\n')
if len(str1) > len(str2):
    num1 = str1.count(str2)
else:
    num1 = str2.count(str1)
print(f'The shorter line is found {num1} time(s) in a longer one')


