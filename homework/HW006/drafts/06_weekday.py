# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# def input_data1():
#     try:
#         return int(input('Please enter number\n'))
#     except:
#         return 0
#
# def check_day(day2):
#     if day2 < 0:
#         print("The number is negative. Don't look back...")
#     elif day2 == 0:
#         print('Are you sure you want to check THAT?')
#     else:
#         day2 %= 7
#         print(list1[day2-1])
#         if (day2 == 6 or day2 == 7):
#             print('Weekend')
#         else:
#             print('Weekday')
#
# print('This program will indicate which day of the week it is based on the number..')
# check_day(input_data1())


list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def input_data1():
    try:
        return int(input('Please enter number\n'))
    except ValueError:
        return 0


def check_day(day2):
    if day2 < 0:
        print("The number is negative. Don't look back...")
    elif day2 == 0:
        print('Are you sure you want to check THAT?')
    else:
        day2 %= 7
        print(list1[day2-1])
        print('Weekend') if day2 == 6 or day2 == 7 else print('Weekday')


print('This program will indicate which day of the week it is based on the number..')
check_day(input_data1())
