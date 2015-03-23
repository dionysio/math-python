from three.A import Turtle, draw_star, draw_polygon
from math import sin, radians, atan, degrees, sqrt, cos, sin
from functools import partial
import svgwrite
from itertools import combinations

length = 100

def inscribed_polygram_rel(turtle, number_of_vertices=5, length=length):
    star_angle = 180 / number_of_vertices
    polygon_side_length = sin(radians(star_angle))/sin(radians(star_angle*2))*length #law of sines

    draw_star(turtle, number_of_vertices, length)
    turtle.right(star_angle*2)
    draw_polygon(turtle, number_of_vertices, length=polygon_side_length)

def inscribed_polygram_abs(turtle, number_of_vertices=5, x=35,y=5, length=length/2):
    vertices = get_polygon_points(number_of_vertices=5, x=x, y=y, length=length)
    for i in combinations(vertices, 2):
        turtle.image.add(turtle.line(i[0], i[1]))

def recursive_squares(turtle, rec_depth=200, offset = 0.2, length=length):
    angle =  degrees(atan(length*offset/(length-length*offset)))
    for i in range(rec_depth):
        for j in range(4): #draw square
            turtle.forward(length)
            turtle.right(90)
        turtle.penup()
        turtle.forward(length*offset)
        turtle.pendown()
        turtle.right(angle)
        _length = length*offset
        length = sqrt(_length**2+(length-_length)**2) #calculate length of inner square

def circle_grid(turtle, length=100, radius=50):
    g = svgwrite.container.Group(clip_path='url(#circle)') #grid
    for x in range(0, length, int(length/10)):
        g.add(turtle.line((0, x), (length, x)))
        g.add(turtle.line((x, 0), (x, length)))

    clip = svgwrite.masking.ClipPath(id='circle')
    clip.add(svgwrite.shapes.Circle((length/2, length/2), r=radius)) #clipping circle
    turtle.image.defs.add(clip)
    turtle.image.add(g)

def recursive_triangles(turtle, rec_depth=12, length=100):
    side = length
    step = 5
    for i in range(rec_depth):
        for i in range(3):
            turtle.forward(side)
            turtle.right(120)
        turtle.penup()
        turtle.right(30)
        turtle.forward(step)
        turtle.left(30)
        turtle.pendown()
        side -= 9 #magic

'''Calculates coordinates for regular polygons
'''
def get_polygon_points(number_of_vertices, start_angle=0, x=255, y=255, length=length, assign_angles=False):
    points =[]
    for i in range(1, number_of_vertices+1):
        angle = i*360/number_of_vertices+start_angle
        rad = radians(angle)
        new_x   = length * cos(rad)
        new_y   = length * sin(rad)
        if assign_angles:
            points.append(((x+new_x, y+new_y), angle))
        else:
            points.append((x+new_x, y+new_y))
        x += new_x
        y += new_y
    return points

def flower_polygon(turtle, number_of_vertices=16, number_of_polygons=16, length=7):
    angle = 360.0/number_of_polygons
    for i in range(0, number_of_polygons):
        turtle.image.add(svgwrite.shapes.Polygon(points=get_polygon_points(number_of_vertices, x=turtle.x+length*7, y=turtle.y+length*7, start_angle=angle*i, length=length), stroke='black', style="fill-opacity:0;"))
        
def draw_object(draw_func, length=length, start_x=65, start_y=65):
    turtle = Turtle(draw_func.__name__+'.svg', start_x=start_x, start_y=start_y)
    draw_func(turtle=turtle)
    turtle.save_image()

if __name__ == "__main__":
    draw_object(draw_func=recursive_triangles, start_x=5, start_y=5)
    draw_object(draw_func=flower_polygon, start_x=0, start_y=0)
    draw_object(draw_func=inscribed_polygram_rel, start_x=5, start_y=40)
    draw_object(draw_func=inscribed_polygram_abs)
    draw_object(draw_func=recursive_squares, start_x=5, start_y=5)
    draw_object(draw_func=circle_grid, start_x=10, start_y=10)