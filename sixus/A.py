from three.B import get_polygon_points
from random import randint
import svgwrite
from PIL import Image
from functools import partial
from bisect import bisect

def middle(p, q, const):
    return int((p[0]+q[0])*const), int((p[1]+q[1])*const)

def get_color(current):
    return (current[0]-7, 255-(current[1]-7),  127)

'''rand_func(from, to) is a function that returns integer between from and to.
color_func(current) is a function that returning color for the current(r,g,b) pixel
'''
def chaos_game(n, scale, length=400, iterations=100000, image=None, rand_func=None, color_func=None, start_x=600, start_y=10):
    if not rand_func:
        rand_func = randint
    if not color_func:
        color_func = lambda x: (0,0,0)
    if not image:
        image = Image.new("RGB", (450, 450), (255, 255, 255))
    vertices = get_polygon_points(number_of_vertices=n, x=start_x, y=start_y, length=length)
    mid = vertices[rand_func(0, n-1)]
    for i in range(iterations):
        chosen = vertices[rand_func(0, n-1)]
        mid = middle(chosen, mid, const=scale)
        try:
            image.putpixel(mid, color_func(mid))
        except:
            pass
    return image

def triangle_chaos():
    image = chaos_game(n=3, scale=0.5, length=400)
    image.save('triangle_chaos.png')

def penta_chaos():
    image =  chaos_game(n=5, scale=3/8, length=500,  color_func=get_color)
    image.save('penta_chaos.png')

def weighted_tetra():
    weights = [3,14,3,14]
    rand_func = partial(weighted_randomness, weights=weights)
    image =  chaos_game(n=4, scale=0.5, length=400,  color_func=get_color, rand_func = rand_func)
    image.save('weighted_tetra.png')


def weighted_randomness(low, high, weights):
    total = sum(weights)
    weights = [sum(weights[:i])+weights[i] for i in range(low,high)]
    return bisect(weights,randint(0,total))


#triangle_chaos()
#penta_chaos()
#penta_chaos()
#weighted_tetra()
