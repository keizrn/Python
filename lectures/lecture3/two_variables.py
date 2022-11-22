# def sum(x, y):
#     return x+y

f = lambda x, y: x + y

# def multi(x,y):
#     return x*y

g = lambda x, y: x * y

def calc(op, a, b):
    print(op(a, b))
    # return(op(a, b))

calc(g, 4, 5)