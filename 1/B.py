# -*- coding: utf-8 -*-
__author__ = 'diony_000'

import matplotlib.pyplot as plt

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


maximums = collatz_maximum(5000)
plt.plot(range(1, len(maximums)+1), maximums, 'ro', markersize=2)
plt.ylim(0, 10000)
plt.savefig('collatz_max.svg')
plt.clf()

maximums = collatz_maximum(5000, modified_version=True)
plt.plot(range(1, len(maximums)+1), maximums, 'ro', markersize=2)
plt.ylim(0, 10000)
plt.savefig('collatz_max_modified.svg')
plt.clf()

avg = collatz_harmonic(8000)
plt.ylim(0, 100)
plt.plot(range(1, len(avg)+1), avg, 'ro', markersize=2)
plt.savefig('collatz_harmonic.svg')
plt.clf()

avg = collatz_harmonic(8000, modified_version=True)
plt.ylim(0, 100)
plt.plot(range(1, len(avg)+1), avg, 'ro', markersize=2)
plt.savefig('collatz_harmonic_modified.svg')
plt.clf()

steps = collatz_steps(100)
plt.plot(range(1, len(steps)+1), steps, 'ro', markersize=2)
plt.savefig('collatz_steps.svg')
plt.clf()