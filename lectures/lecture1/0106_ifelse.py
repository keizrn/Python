# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Наташа':
    print('You are finally here, Natasha!')
elif username == 'Миша':
    print('Welcome home, Misha')
else:
    print('Hello,', username)