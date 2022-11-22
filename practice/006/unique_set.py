# Дана последовательность чисел.
# Получить отсортированный по возрастанию список уникальных элементов заданной последовательности.

import script004

def list_sort(list_1):
    print(list_1)
    print(sorted(set(list_1)))
    list_unique = [i for i in list_1 if list_1.count(i) == 1]
    print(sorted(list_unique))

list_sort(script004.random_list(10, 0, 10))


