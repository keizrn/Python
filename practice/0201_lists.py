# lists

from unittest.util import _count_diff_all_purpose


colors = ['red', 'green', 'white']
print(type(colors))
print(colors)

colors.append('black') # add to the end of the list
print(colors)

colors.insert(2, 'gray') # insert element
print(colors)

print()
position = colors.index('green') # find element
print(position)

if 'violet' in colors:
    position2 = colors.index('violet')
    print(position2)
else:
    print('no such element: Violet')

print()
colors.remove('gray') # delete 1st such element
print(colors)

# pop???

colors.append('gray')
colors.append('red')
colors.append('green')
count_green = colors.count('green')
print(colors)
print(f'There are {count_green} green colors in the list')

print()
print(id(colors), colors)
colors.reverse() # reverse
print(id(colors), colors)

print()
colors.sort()
print(id(colors),colors)

