#

lst = [8, 5, 2, 3, 4, 6, 1, 7]
fst = min(lst[0], lst[1])
lst2 = [fst]
i = 2
while i < len(lst):
    if lst[i] > fst:
        lst2.append(lst[i])
        fst = lst[i]
    i += 1
print(lst2)