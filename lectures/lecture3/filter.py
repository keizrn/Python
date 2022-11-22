data = [x for x in range(20)]

res = list(filter(lambda x: not x % 2, data))
print(res)
