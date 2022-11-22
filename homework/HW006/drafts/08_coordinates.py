# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def input_coord(n):
    try:
        return int(input(f'Input {n} coordinate.. \n'))
    except:
        print('Wrong input')
        return(breakpoint)


def define_quarter(x2, y2):
    if not(y2 == breakpoint or x2 == breakpoint):
        if y2 == 0:
            print('Center') if x2 == 0 else print('Axis X')
        elif x2 == 0:
            print('Axis Y')
        elif x2 > 0:
            if y2 > 0:
                print('Quarter 1')
            elif y2 < 0:
                print('Quarter 4')
        elif x2 < 0:
            if y2 > 0:
                print('Quarter 2')
            elif y2 < 0:
                print('Quarter 3')


# def define_quarter(x2, y2):
#     if not(y2 == breakpoint or x2 == breakpoint):
#         if y2 == 0:
#             if x2 == 0:
#                 print('Center')
#             else:
#                 print('Axis X')
#         elif x2 == 0:
#             print('Axis Y')
#         elif x2 > 0:
#             if y2 > 0:
#                 print('Quarter 1')
#             elif y2 < 0:
#                 print('Quarter 4')
#         elif x2 < 0:
#             if y2 > 0:
#                 print('Quarter 2')
#             elif y2 < 0:
#                 print('Quarter 3')

print('This program will indicate # of quarter based on coordinates.')
define_quarter(input_coord('1st'),input_coord('2nd'))