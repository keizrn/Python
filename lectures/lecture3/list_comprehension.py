# list = []
#
# for i in range(1, 101):
#     #if(i%2 == 0):
#     list.append(i)

f = lambda x: x**3

list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)