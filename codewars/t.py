from itertools import *


def should_drop(x):
    print('Testing:', x)
    return False


for i in dropwhile(should_drop, [-1, 0, 0, 2, -2]):
    print(i)

list(dropwhile(should_drop, [-1, 0, 0, 2, -2]))
