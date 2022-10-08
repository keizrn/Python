# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def input_data1():
    try:
        day1 = int(input('Please enter number\n'))
        return day1
    except:
        return 0

def check_day(day2):
    if day2 < 0:
        print("The number is negative. Don't look back...")
    elif day2 == 0:
        print('Are you sure you want to check THAT?')
    else:
        day2 %= 7
        print(list1[day2-1])

print('This program will indicate if the day of the week it is based on the number..')
check_day(input_data1())
