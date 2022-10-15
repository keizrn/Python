# арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# () Скобки меняют приоритет

a = 2
b = 3
print(a + b) # Сумма

a = 123
b = -122
print(a + b) # Sum with a negative

a = 4
b = 4
print(a * b) # Multiplication

a = 2
b = 8
print(a / b) # Division

a = 12
b = 8
print(a // b) # деление в целых числах

a = 15
b = 9
print(a % b) # Remainder

a = 2
b = 8
print(a ** b) # возведение в степень

print('\nПроблема с хранением чисел в системе:')
a = 1.3
b = 3
print(a * b)

print('\nВариант решения - простое округление:')
print(round(a * b, 5))



