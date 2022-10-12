# Реализуйте алгоритм перемешивания списка.

from random import random, randrange


def random_list():
    word_list = ['brake', 'club', 'river', 'grass', 'damp', 'drown', 'treatment', 'lock', 'branch', 
'frightened', 'cross', 'life', 'confess', 'film', 'lethal', 'cultured', 'tidy', 'station', 'grouchy', 'supreme', 'queue', 'noisy', 'trucks', 'unfasten', 'yoke', 'actor', 'sloppy', 'color', 'insect', 'empty', 'able', 'basin', 'lethal', 'escape', 'handy', 'tough', 'pain', 'sniff', 'shop', 'paper', 'ocean', 'island', 'straw', 'enchanted', 'punishment', 'solid', 'pleasant']
    rand_list = []
    leng_1 = randrange(3,10)        # random list of 3 to 10 words
    i = 0
    temp = 0
    while i < leng_1:               # filling in new list
        temp = randrange(0,len(word_list)-1)
        rand_list.append(word_list[temp])
        word_list.remove(word_list[temp])
        i += 1
    print(f'Initial list is:\n{rand_list}')
    shuffle_list(rand_list)

def shuffle_list(old_list):
    len_1 = len(old_list)
    new_list = []
    temp2 = 0
    for i in range(0,len_1):
        temp2 = randrange(0,len(old_list))
        new_list.append(old_list[temp2])
        old_list.remove(old_list[temp2])
    print(f'\nNew list is:\n{new_list}')
    repeat_1 = input('Would you like to shuffle again? Y/N..\n').lower()
    if (repeat_1 == 'y'):
        shuffle_list(new_list)

random_list()