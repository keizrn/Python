#

a = {1, 2, 3, 4, 5, 6}
b = {2, 5, 8, 13, 21, 34}
c = a.copy()
u = a.union(b)
i = a.intersection(b)
dl = a.difference(b)
dr = b.difference(a)

q = a \
    .union(b) \
    .difference(a.intersection(b))

print(f'a = {1, 2, 3, 4, 5, 6}')
print(f'b = {2, 5, 8, 13, 21, 34}')
print(f'\na.union(b) = {a.union(b)}')
print(f'a.intersection(b) = {a.intersection(b)}')
print(f'a.difference(b) = {a.difference(b)}')
print(f'b.difference(a) = {b.difference(a)}')

