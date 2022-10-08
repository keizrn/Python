# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

def input_coord(n, m):
    try:
        return int(input(f'Input {n} coordinate of the {m} point.. \n'))
    except:
        return(breakpoint)

def define_length(x1, y1, x2, y2):
    if (x1 == breakpoint or y1 == breakpoint or x2 == breakpoint or y2 == breakpoint):
        print('Wrong input')
    else:
        print(f'Distance between 2 points is {round(((x2 - x1)**2 + (y2 - y1)**2)**0.5,2)}')

print('This program will calculate length of the line based on coordinates.')
define_length(input_coord('1st', '1st'),input_coord('2nd', '1st'),input_coord('1st','2nd'),input_coord('2nd','2nd'))