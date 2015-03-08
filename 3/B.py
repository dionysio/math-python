from A import Turtle, draw_star, draw_polygon
from math import sin, radians, atan, degrees, sqrt, cos
from functools import partial
import svgwrite

def inscribed_polygram_rel(turtle, number_of_vertices=5, length=100):
    star_angle = 180 / number_of_vertices
    polygon_side_length = sin(radians(star_angle))/sin(radians(star_angle*2))*length #law of sines, next time use the fucking radians!!!

    draw_star(turtle, number_of_vertices, length)
    turtle.right(star_angle*2)
    draw_polygon(turtle, number_of_vertices, length=polygon_side_length)


def inscribed_polygram_abs(turtle, number_of_vertices=5, length=100):
    star_angle = 180 / number_of_vertices
    polygon_side_length = sin(radians(star_angle))/sin(radians(star_angle*2))*length #law of sines, next time use the fucking radians!!!

    draw_star(turtle, number_of_vertices, length)
    points = turtle.points
    for i in range(number_of_vertices-2): #draw polygon lines
        turtle._draw_line_abs(points[i], points[i+2])
        if i+3 < number_of_vertices:
            turtle._draw_line_abs(points[i], points[i+3])


def recursive_squares(turtle, rec_depth=200, offset = 0.2, length=100):
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

def circle_grid(turtle, n=6, length=100): #length is radius
    cp = svgwrite.Drawing().clipPath(id="clip-circle")
    cp.add(svgwrite.shapes.Circle(cx="255", cy="255", r=length))
    pattern = svgwrite.pattern.Pattern(id="grid-pattern", x="0", y="0", width=length/n, height=length/n, patternUnits="userSpaceOnUse")
    rect = svgwrite.shapes.Rect(x="0", y="0", width=length/n, height=length/n )
    pattern.add(rect)
    turtle.image.defs.add(pattern)
    turtle.image.defs.add(cp) #clipping circle
    group = svgwrite.container.Group(clip_path="url(#clip-circle)")
    rect_cp = rect.copy()
    rect_cp.fill('url(#grid-pattern)')
    group.add(rect_cp)
    turtle.image.add(group)
    turtle.save_image()

def recursive_triangles(turtle, rec_depth=20, length=10):
    stroke_width = length/100
    A_x, A_y = turtle.x, turtle.y
    B_x, B_y = turtle.x+length, turtle.y
    C_x, C_y = turtle.x+length/2, turtle.y + sqrt(length**2-(length/2)**2) #ugly sqrt expression is basically altitude of the triangle
    center_x, center_y = ((A_x+B_x+C_x)/3,(A_y+B_y+C_y)/3)  #calculate centroid
    print(center_x, center_y)
    turtle.image.add(svgwrite.shapes.Polygon(id="original", points=[(A_x,A_y), (B_x, B_y),(C_x, C_y)], stroke='black', style="fill-opacity:0;stroke-width: %f" % stroke_width))
    for i in range(2,rec_depth):
        turtle.image.add(svgwrite.container.Use(href="#original", transform="translate(%d, %d) scale(%d)" % ((1-i)*center_x,(1-i)*center_y,i), style="stroke-width: %f" % (stroke_width/i,)))


def draw_object(turtle, draw_func):
    turtle.clear_image(draw_func.__name__+'.svg')
    draw_func(turtle=turtle)
    turtle.save_image()


turtle = Turtle(None) #reusing the same turtle object
draw_function = partial(draw_object, turtle=turtle)

'''
draw_function(draw_func=inscribed_polygram_rel)
draw_function(draw_func=inscribed_polygram_abs)
draw_function(draw_func=recursive_squares)
draw_function(draw_func=recursive_triangles)'''

draw_function(draw_func=circle_grid)