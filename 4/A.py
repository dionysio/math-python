from PIL import Image, ImageChops
from math import pi, sin, cos, sqrt, fabs
from functools import partial
from B import polygon

dimension = 500
length = 100


def filled_circle():
    image = parametric_shape(circle_equation, filled=True)
    image.save('filled_circle.png')

def circle():
    image = parametric_shape(circle_equation)
    image.save('circle.png')

def rainbow_spiral():
    color_func = lambda x: (int(255*(1-x)),int(127*(x)),int(255*(x))) #rainbow colors
    image = parametric_shape(spiral_equation, color_func=get_rainbow_color, irx=int(length*0.9), iry=int(length*0.9), filled=True)
    image.save('rainbow_spiral.png')

def rainbow_triangle():
    mid = (length/2, sqrt(length**2-(length/2)**2))
    color_func = lambda x,y: (int((255*x)/(length)), int((255*y)/(mid[1])), 255-int((255*x)/(length)))
    image = polygon([(0,0), mid, (length,0)], color_func = color_func)
    image.save('rainbow_triangle.png')

def ellipse():
    rx = length
    ry = int(length/3)
    color_func = lambda x: (int((x)*255),int((x)*255),int((x)*255))
    image = parametric_shape(circle_equation, filled=True, rx=rx, ry=ry, color_func=color_func)
    image.save('ellipse.png')

def circle_equation(angle):
    return (cos(2*pi*angle), sin(2*pi*angle))

def spiral_equation(angle, spirality = 5): #is spirality a word?
    new_angle = 2*pi*angle*spirality
    return (angle*cos(new_angle), angle*sin(new_angle))

'''
slices - how accurate should drawing be (higher the number, higher the final granularity will be)
rx - outside radius of shape on x-axis
ry - outside radius of shape on y-axis
irx - inside radius of shape on x-axis
iry - inside radius of shape on y-axis
color_func - function to get color for point
cx - center of the shape on x-axis
cy - center of the shape on y-axis
filled - bool, should be shape filled in
'''
def parametric_shape(parametric_equation, slices=1000, image=None, color_func=None, rx=length, ry=length, irx=0, iry=0, cx=dimension/2, cy=dimension/2, filled=False):
    if not image:
        image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    if not color_func:
        color_func = lambda x: (0,0,0) #simple black
    for i in range(slices):
        angle = i/slices #one slice
        for j in range(rx, irx, -1): #if filled is False, this runs only on once to draw the outer radius of the shape
            for k in range(ry, iry, -1):
                shift_x, shift_y = parametric_equation(angle)
                x,y = int(cx+j*shift_x), int(cy+k*shift_y)
                color = color_func(((x-cx)**2)/(rx*rx)+((y-cy)**2)/(ry*ry))
                try:
                    image.putpixel((x, y), color)
                except IndexError:
                    continue
                if not filled:
                    break
            if not filled:
                break
    return image

filled_circle()
circle()
#rainbow_spiral()
#rainbow_triangle()
#ellipse()