# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def input_data():
    try:
        quarter = int(input('input # of quarter from 1 to 4..\n'))
        if quarter in range(1,5):
            return quarter
        else:
            return breakpoint
    except:
        return breakpoint

def coordinates(quar1):
    if quar1 == breakpoint:
        print('Your input was incorrect')
    elif quar1 == 1:
        print('x & y might be from 0 to +inf')
    elif quar1 == 2:
        print('x might be from -inf to 0, y from 0 to +inf')
    elif quar1 == 3:
        print('x & y might be from -inf to 0')
    else:
        print('x might be from 0 to +inf, y from -inf to 0')

print('This program will give you a range of possible coordinates for x & y based on the # of quarter you input.')
coordinates(input_data())