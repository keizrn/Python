file_1 = open('file.txt.', 'r', encoding='utf8')
data_1 = list(map(int, file_1.readline().split()))
file_1.close()

result_1 = filter(lambda x: not x % 2, data_1)
result_1 = list(map(lambda x: (x, x**2), result_1))

print(result_1)