colors = {'red', 'green', 'blue'}
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# colors.remove('red') # KeyError - 'red' does not exist

colors.discard('red') # safe delete

colors.clear()
print(colors)


