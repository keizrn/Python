# while, for cycles

# original = int(input('Input any number to be inverted..'))
original = 532
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Выходим из цикла')
print(inverted)

print('\nNow For cycle:')
list = [1, 2, 3, 4, 10, 5]
for i in list:
    print(i)

print('\nNow with range:')
list = range(5)
for i in list:
    print(i)

print('\nNow a more complicated range:')
list = range(1, 10, 2)
for i in list:
    print(i)