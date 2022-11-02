
from itertools import groupby

file_2 = open('output1.txt', 'w', encoding='utf8')

with open('test1.txt', 'r', encoding='utf8') as f:
    for line_1 in f:
        string_temp_2 = ""
        print(line_1)
        for i_1 in range(0, len(line_1)-1, 2):
            #print(line_1[i_1])
            string_temp_2 += line_1[i_1]*int(line_1[i_1+1])
        print(string_temp_2)
        file_2.writelines(f"{string_temp_2}\n")

print(f.closed)
print(file_2.closed)