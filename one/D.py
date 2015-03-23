# -*- coding: utf-8 -*-
__author__ = 'diony_000'
from PIL import Image
from functools import partial

def gcd_mod(a,b):
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

def get_color(number, maximum):
    return (0, 255-int(number/maximum * 255), 255)

def save_gcd(func, is_steps=1, result_factor=1, result_maximum=10):
    dimension = 480
    image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    for i in range(1,dimension):
        for j in range(1, dimension):
            result = func(i,j)[is_steps]
            image.putpixel((i,j), get_color(result*result_factor, maximum=result_maximum))
    image = image.rotate(90)
    image.save("gcd_%s.png" % str(result))


save_gcd(gcd_substract, is_steps=0, result_factor=5, result_maximum=480)

save_gcd(gcd_substract, result_factor=5, result_maximum=958)
save_gcd(gcd_mod, result_maximum=13)