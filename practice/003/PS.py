# def check_num_in_list(numb):
#     list_1 = [1, 2, 3, 5, 45, 6, 7, 9, 11]
#     return int(numb) in list_1

# print(check_num_in_list(input('input number..\n')))




# # Вывести список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.
# # numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

# list_2 = []
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45, (81, 80, 39, 32), (1, 2, 3, 4), (90, 10)))



# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# def count_second_incl(num):
#     list_3 = ["23", "34", "45", "23", "45", "64", "34"]
#     ind = list_3.index(num)
#     for item in range(ind+1, len(list_3)):
#         if list_3[item] == num:
#             print(item)
#             return
#     print(f'no second inclusion of {num}')

# count_second_incl(input(f'Input number to find second inclusion..\n'))

# Создать базу данных для продукта: id, name, date
# Сделать функционал для пользователя:
# Предложить выбор: удаление, добавление, поиск товара по id, выход из программы

# dict_1 = {'1' : {'name':'Bob', 'date':'09-10-2022'},
#         '2' : {'name':'Alena', 'date':'05-11-2021'},
#         '3' : {'name':'Dmitry', 'date':'04-03-2022'}}