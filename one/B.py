# -*- coding: utf-8 -*-
__author__ = 'diony_000'

import matplotlib.pyplot as plt
from functools import partial

def collatz(num, modified_version=False):
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num //= 2 #int division
        elif modified_version:
            num = (3*num+1)//2
        else:
            num = 3*num+1
    sequence.append(1)
    return sequence

def collatz_loop(upper_bound, func, second_func=None, modified_version=False):
    result = []
    if second_func:
        for i in range(1, upper_bound):
            c = collatz(i, modified_version)
            result.append(func(c)/second_func(c))
    else:
        for i in range(1, upper_bound):
            result.append(func(collatz(i,modified_version)))
    return result

def collatz_steps(upper_bound, modified_version=False):
    return collatz_loop(upper_bound, len, modified_version=modified_version)

def collatz_maximum(upper_bound, modified_version=False):
    return collatz_loop(upper_bound, max, modified_version=modified_version)

def collatz_avg(upper_bound, modified_version=False):
    return collatz_loop(upper_bound, sum, len, modified_version)

def inverse_sum(lst):
    total=0
    for num in lst:
        total+=1/num
    return total

def collatz_harmonic(upper_bound, modified_version=False):
    return collatz_loop(upper_bound, len, inverse_sum, modified_version)

my_plot = partial(plt.plot, marker='o', color='red', markersize=2, ls=' ') #plot with red circles representing individual points
upper_bound = 8000 #basically how many iterations to do

###

func=collatz_maximum
maximums = func(upper_bound)
my_plot(range(1, len(maximums)+1), maximums)
plt.ylim(0, 10000)
plt.title('collatz_max')
plt.savefig('collatz_max.svg')
plt.clf()

maximums = func(upper_bound, modified_version=True)
my_plot(range(1, len(maximums)+1), maximums)
plt.ylim(0, 10000)
plt.title('collatz_max_modified')
plt.savefig('collatz_max_modified.svg')
plt.clf()

###

func=collatz_harmonic
avg = func(upper_bound)
plt.ylim(0, 100)
my_plot(range(1, len(avg)+1), avg)
plt.title('collatz_harmonic')
plt.savefig('collatz_harmonic.svg')
plt.clf()

avg = func(upper_bound, modified_version=True)
plt.ylim(0, 100)
my_plot(range(1, len(avg)+1), avg)
plt.title('collatz_harmonic_modified')
plt.savefig('collatz_harmonic_modified.svg')
plt.clf()

###

steps = collatz_steps(upper_bound)
my_plot(range(1, len(steps)+1), steps)
plt.title('collatz_steps')
plt.savefig('collatz_steps.svg')
plt.clf()