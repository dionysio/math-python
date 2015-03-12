from A import parametric_shape, circle_equation, spiral_equation
from PIL import Image, ImageChops, ImageFilter
import operator
from functools import partial

dimension = 500

def draw_square(start_x, start_y, a, b, color, image=None):
    if not image:
        image = Image.new("RGB", (dimension, dimension), (0, 0, 0))
    for i in range(a):
        for j in range(b):
            x, y=(start_x+i,start_y+j)
            image.putpixel((x, y), color)
    return image

def checkerboard(image=None):
    if not image:
        image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    for i in range(0, dimension, int(dimension/10)):
        for j in range(0, dimension, int(dimension/10)):
            if (i+j) % (int(dimension/5)) == 0:
                draw_square(i, j, int(dimension/10), int(dimension/10), color=(0,0,0), image=image)
    return image

def blurred_circles(number_of_circles=9, width=12, step = 40):
    first_image=None
    for i in range(0, number_of_circles):
        inside_radius = i*step
        first_image = parametric_shape(circle_equation, image=first_image, rx=inside_radius+width, ry=inside_radius+width, irx=inside_radius, iry=inside_radius, filled=True, slices=1000) #draw one circle
    second_image =  draw_square(int(dimension/8), int(dimension/8), int(dimension-dimension/4), int(dimension-dimension/4), color=(255,255,255))
    image = ImageChops.difference(first_image, second_image) #bit of a cheat
    image = image.filter(ImageFilter.GaussianBlur(radius=3))
    image.save('blurred_circles.png')

def donut_checkerboard():
    first_image = checkerboard()
    second_image = parametric_shape(circle_equation, rx=175, ry=175, irx=90, iry=90, filled=True, slices=1000)
    image = ImageChops.difference(first_image, second_image) #bit of a cheat
    image.save('checkboard.png')

def spiral_checkboard(radius=300, width = 12):
    first_image = parametric_shape(spiral_equation, image=None, rx=radius, ry=radius, irx=radius-width, iry=radius-width, filled=True, slices=10000) #draw one circle
    second_image = checkerboard()
    image = ImageChops.difference(first_image, second_image)
    image.save('spiral_checkboard.png')

donut_checkerboard()
spiral_checkboard()
blurred_circles()