#

capitals = {'Russia': 'Moscow', 
            'France': 'Paris', 
            'Great Britain': 'London'}

for key, value in capitals.items():
    print(key, '\t-/-', value)

if 'Russia' in capitals:
    print('\nRussia is among countries in the dictionary')

item1 = capitals.get('Estonia', 'No Estonia in the dictionary')
print(item1)

capitals['Kazakhstan'] = 'Nursultan'
print('\n')

for key, value in capitals.items():
    print(key, '\t-/-', value)

del capitals['Kazakhstan']
print('\n')

for key, value in capitals.items():
    print(key, '\t-/-', value)

capitals['Kazakhstan'] = 'Almaty'
print('\n')

for key, value in capitals.items():
    print(key, '\t-/-', value)