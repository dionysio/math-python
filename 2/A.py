from copy import copy
from itertools import repeat, chain

def permutations(data):
    variations(data, n = len(data)+1)


def variations(data, target='', n=None):
    global variats
    if n is None:
        n = len(data)+1
    for i in range(len(data)):
        new_target = target+data[i]
        if len(new_target) <= n:
            #if len(new_target)+1 == n:
            variats.add(new_target)
            variations(data[i+1:],new_target, n)


def variations_with_repetition(data, n):
    data = ''.join(chain.from_iterable(repeat(data, n)))
    variations(data, n=n)


data = 'abcda'
variats = set() #global variable for different combinations
permutations(data)
print(variats)
#variats.clear()
#variations(data)
