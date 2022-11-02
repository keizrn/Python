
from itertools import groupby

file_1 = open('input1.txt', 'r', encoding='utf8')

with open('test1.txt', 'w', encoding='utf8') as f:
    for line_1 in file_1:
        string_temp = ""
        for x_1, y_1 in groupby(line_1.rstrip()):
            #print(sum(1 for _ in y_1))
            sum_1 = sum(1 for _ in y_1)
            while sum_1 > 9:
                string_temp += f"{x_1}9"
                sum_1 -= 9
            string_temp += f"{x_1}{sum_1}"
            print(string_temp)
        f.writelines(f"{string_temp}\n")
    print(f.mode)
print(f.closed)

file_1.close()