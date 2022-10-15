# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # no separators
# data.write('\nLine12\n')
# data.write('Line13\n')
# data.close()


# exit()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close

exit()


# book = open('voyna-i-mir-tom-1.txt','r').read()
# search = 'Ната'
# if search in book:
#     print(book.count(search))
