from random import random, randrange


def flip_coin():
    coin = randrange(1, 3)
    if coin == 1:
        return "Hats", 1
    else:
        return "Tails", 2
