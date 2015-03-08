# -*- coding: utf-8 -*-
__author__ = 'diony_000'
from PIL import Image
from functools import partial

def gcd_mod_recursive(a, b, counter=0):
    if b == 0:
        return (a, counter)
    else:
        return gcd_mod(b, a%b, counter+1)

def gcd_mod_iterative(a,b):
    counter = 0
    while b != 0:
        counter += 1
        a, b = (b, a%b)
    return a, counter

def gcd_substract(a, b):
    counter=0
    while a != b:
        counter += 1
        if a > b:
           a = a - b
        else:
           b = b - a
    return (a, counter)

def get_color1(number, maximum):
    return (0, 255-int(number/maximum * 255), 255)

def get_color2(number):
    return (255, number % 255, 0)

def save_gcd(func, color_func):
    dimension = 480
    image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    for i in range(1,dimension):
        for j in range(1, dimension):
            steps = func(i,j)[1]
            image.putpixel((i,j), color_func(steps))
    image = image.rotate(90)
    image.save("gcd_%s.png" % str(steps))


save_gcd(gcd_substract, get_color2)
save_gcd(gcd_mod_iterative, partial(get_color1, maximum=13))