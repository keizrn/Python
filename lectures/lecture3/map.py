# data_1 = [x for x in range(1, 20)]

data_1 = list(map(int, input().split()))

li = map(lambda x: x + 10, data_1)

print(*li)