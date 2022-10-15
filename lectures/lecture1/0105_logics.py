# logical operations
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in



a = 1 > 4
print(a)

b = not a
print(a == b)

a = 1 < 3 < 5 < 7 < 9
print(a)

print('\nДизъюнкция истинна тогда и только тогда, когда истинно хотя бы одно из высказываний A или B.')
print('Другими словами, дизъюнкция ложна тогда и только тогда, когда ложны оба высказывания A и B.')
print('f = 1 < 2 or 3 < 2')
print('print(f)')
f = 1 < 2 or 3 < 2
print(f)

print()
f = [1, 2, 3, 4]
print(f)
print('2 in f?')
print(2 in f)
print('not 2 in f?')
print(not 2 in f)

is_odd = not f[0] % 2 # отрицание 1 - это 0
print(is_odd)