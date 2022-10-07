# Типы данных и переменные 
# int, float, boolean, str, list, None

a = 123
# print(a)
# print(type(a))

b = 1.23
# print(b)
# print(type(b))

value = None
# print(type(value))
value = 1234
# print(type(value))

s = 'qwerty \'hello world\'' # \n - перенос строки \' - одинарная кавычка
print(a, '-', b, '-', s) # вывод строки
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')

print()
print('{1} - {2} - {0}'.format(a, b, s)) # поменять порядок вывода переменных

f = True
print(f)

print()
print('Поработаем с массивами\n')
list = ['1', '2', '3', '4', 'hello'] # это массив строк
print(list)

a, b, c = 1, 2, 5 # множественное присваивание
