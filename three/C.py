from A import Turtle, draw_polygon
from B import draw_object, get_polygon_points
from functools import partial
from math import sqrt, pi, sin, cos
import svgwrite

length = 100

def snowflake(turtle, length=length, level=5, angle=60):
    if level:
        length /= 3.0
        snowflake(turtle, length, level=level-1, angle=angle)
        turtle.left(angle)
        snowflake(turtle, length, level=level-1, angle=angle)
        turtle.right(angle*2)
        snowflake(turtle, length, level=level-1, angle=angle)
        turtle.left(angle)
        snowflake(turtle, length, level=level-1, angle=angle)
    else:
        turtle.forward(length)
        return        

def koch_snowflake(turtle, length=length, level=5):
    for i in range(3):
        snowflake(turtle, length)
        turtle.right(120)


def n_flake(turtle, n=5, level=3, length=length/2, points=None, scale=None):
    if not scale:
        scale = (3-sqrt(5))/2
    if not points:
        points = get_polygon_points(n, x=80, y=5, length=length, assign_angles=True) #first outside polygon
    if level:
        '''height = (length/(2*sin(pi/5)))*(1+cos(pi/5))*(1-scale) #radius*shift*scale gets us what we must shift y-axis to get to the nth point
        points.append(((points[1][0][0], points[1][0][1]-height),180-points[1][1]))'''
        for anchor_point in points:
            new_points = get_polygon_points(n, start_angle=anchor_point[1], x=anchor_point[0][0], y=anchor_point[0][1], length=length*scale, assign_angles=True)
            n_flake(turtle, n, level-1, length*scale, new_points) #start another level inside
    else:
        turtle.image.add(svgwrite.shapes.Polygon(points=[point[0] for point in points], stroke='black', style="fill-opacity:0;"))
    
def sierpinski_triangle(turtle, level=6, length=length):
    if level<=0: 
        return
    half_length = 0.5*length

    if level > 1:
        sierpinski_triangle(turtle, level-1, half_length)
        turtle.move(half_length)
        sierpinski_triangle(turtle, level-1, half_length)
        turtle.left(120)
        turtle.forward(half_length)
        turtle.right(120)
        sierpinski_triangle(turtle, level-1, half_length)
        turtle.right(120)
        turtle.move(half_length)
        turtle.left(120)
    draw_polygon(turtle, 3, length) #outside triangle

def tree(turtle, level=10, length=length/2, angle=45):
    turtle.forward(length)
    turtle.left(angle)

    if level: 
        tree(turtle, level-1, length*0.55)
    turtle.right(angle*2)
    if level: 
        tree(turtle, level-1, length*0.55)
    turtle.left(angle)
    turtle.move(-length)

draw_object(draw_func=n_flake, length=300)
'''
draw_object(draw_func=sierpinski_triangle, start_x=2, start_y=90)
draw_object(draw_func=koch_snowflake, start_x=2, start_y=35)
draw_object(draw_func=tree, start_x=5)'''