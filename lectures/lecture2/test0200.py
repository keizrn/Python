#

from typing import ItemsView


def new_string(symbol, count = 3):
    return symbol*count

def concatenatio(*params):
    res: str = ""   # type indication, optional
    for item in params:
        res += item
    return res