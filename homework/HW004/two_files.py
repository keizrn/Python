# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, 
# значения — данные о хобби.

dict_names_hobbies = {}
file_1 = open('names.txt', 'r', encoding='utf-8')
file_2 = open('hobbies.txt', 'r', encoding='utf-8')
for (line_1, line_2) in zip(file_1, file_2):
    dict_names_hobbies[str(line_1).rstrip()] = str(line_2).rstrip()
print("\033[01m\033[04mNames".ljust(45), "Hobbies\033[00m")
for i1 in dict_names_hobbies:
    print(i1.ljust(35),dict_names_hobbies[i1])
file_1.close()
file_2.close()