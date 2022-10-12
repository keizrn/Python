# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication_List(number):
    list = []
    temp = 1
    for i in range(1,number+1):
        temp *= i
        list.append(temp)
    print(f'Factorials are: {list}')


print('This program will show a list of factorials from 1 till the number you input.')
multiplication_List(int(input('Please input positive integer number..\n')))


