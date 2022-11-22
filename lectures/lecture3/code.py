def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

file_1 = open('file.txt.', 'r', encoding='utf8')
data_1 = file_1.readline().split()
file_1.close()

res = select(int, data_1)
print(res)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)
print(res)


# for i_1 in range(len(my_list)):
#     my_list[i_1] = int(my_list[i_1])
#
# f = lambda x: x**2
# my_list_2 = [(i, f(i)) for i in my_list if i % 2 == 0]
# print(my_list_2)
