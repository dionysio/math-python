from math import sqrt, hypot
from random import random

precision=3500000


'''Archimedes got 7 decimal places right, Leibniz only 6, Monte Carlo is all over the place with the precision, mostly it got 2-3 places right (might also have something to do with implementation). Archimedes is also much faster than the other two
'''

'''3.1415929393040165
'''
def leibniz():
    total = 0
    for i in range(1,precision):
        if i % 2:
            total += 1/(i*2-1)
        else:
            total -= 1/(i*2-1)
    print(total*4)

'''
3.141592692092259
but much much faster than monte_carlo
'''
def archimedes():   
    x = 4
    y = 2*sqrt(2)
    while x-y > 1/precision:
        x,y = (2*x*y/(x+y), sqrt(2*x*y*y/(x+y)))
    print((x+y)/2)


'''
3.1430009302325583
3.141973953488372
3.141832558139535
3.1419888372093023
3.1428837209302327
3.143164651162791
3.1434251162790696
3.141931162790698
3.1432372093023258
3.141248372093023
'''
def monte_carlo():
    count_inside = 0
    for count in range(0, precision):
        d = hypot(random(), random())
        if d < 1: 
            count_inside += 1
    count += 1
    print( 4.0 * count_inside / count)
