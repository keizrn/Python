# Задайте список из n чисел последовательности (1+1/n)^n и выведите на 
# экран их сумму.

def dict_formula(num):
    dict_1 = {}
    for i in range(1,num+1):
        dict_1[i] = round((1 + 1/i)**i, 2)
    print(dict_1)

print('This program will give you a dictionary of values for x & y in f(x) = (1 + 1/x)^x from 1 till the number you input.')
try:
    num1 = int(float(input('Please input integer number higher than 0:\n')))    # real number will be rounded to the nearest integer
    if num1 < 1:
        print('Your number is too low.')
    else:
        dict_formula(num1)
except:
    print('Your input was not correct.')