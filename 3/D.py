from A import Turtle
from functools import partial
from math import degrees,atan
from B import draw_object
from C import snowflake, n_flake

length=50

def wheel(turtle, rec_depth=84, offset = 0.2, length=length):
    angle =  degrees(atan(length*offset/(length-length*offset)))
    for i in range(rec_depth):
        for j in range(4): #draw square
            turtle.forward(length)
            turtle.right(90)
        turtle.penup()
        turtle.forward(length*offset)
        turtle.pendown()
        turtle.right(angle)


def cesaro_snowflake(turtle, length=length, number_of_vertices=5):
    length *= 9
    for i in range(number_of_vertices):
        snowflake(turtle, length, level=5, angle=85)
        turtle.left(360/number_of_vertices)

def half_septaflake():
    draw_func = partial(n_flake, n=7, level=2, length=50, points=None, scale=1/2)
    draw_func.__name__= 'half_septaflake'
    draw_object(draw_func=draw_func, length=300)
        
draw_object(draw_func=wheel, start_x=65, start_y=25)
draw_object(draw_func=cesaro_snowflake, start_x=35, start_y=145)
half_septaflake()