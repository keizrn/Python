#

from turtle import left


dictionary = {}
dictionary = \
    {
        'up': 'fly',
        'down': 'dig',
        'right': 'go',
        'left': 'ride'
    }

print(dictionary)
print(dictionary['left'])

for k in dictionary:
    print(k)

del dictionary['left']
print('\n',dictionary)

dictionary['left'] = 'swim'
print('\n',dictionary)