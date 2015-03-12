from math import radians, cos, sin
import svgwrite 
from functools import partial
length = 100
dimension = 500

class Turtle():
    def __init__(self, filename = 'turtle.svg', start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y
        self.angle = 0.0
        self.draw = True
        self.image = svgwrite.Drawing(filename, viewBox= "%s, %s, %s, %s" % (0, 0, length*1.5, length*1.5), preserveAspectRatio="xMinYMin meet") #self.x-length*0.5, self.y-length*0.5
        self.line = partial(svgwrite.shapes.Line, stroke='black') #stroke_width=length/350

    def penup(self):
        self.draw = False

    def pendown(self):
        self.draw = True

    def _draw_line(self, target_x, target_y):
        self.image.add(self.line((self.x, self.y), (target_x, target_y)))

    def save_image(self):
        self.image.save()

    def move(self, step):
        self.penup()
        self.forward(step)
        self.pendown()

    def forward(self, step):
        rad = radians(self.angle)
        new_x   = step * cos(rad)
        new_y   = step * sin(rad)
        if self.draw:            
            self._draw_line(self.x+new_x, self.y+new_y)
        self.x += new_x
        self.y += new_y

    def right(self, angle):
        self.change_angle((self.angle + angle) % 360)

    def left(self, angle):
        self.change_angle((self.angle - angle) % 360)

    def change_angle(self, angle):
        self.angle = angle

def draw_polygon(turtle, number_of_vertices=6, length=length/2):
    angle = 360.0/number_of_vertices
    for i in range(number_of_vertices):
        turtle.forward(length)
        turtle.left(angle)

def draw_star(turtle, number_of_vertices=9, length=length):
    angle = 180.0 - 180.0 / number_of_vertices
    for i in range(number_of_vertices):
        turtle.forward(length)
        turtle.right(angle)

turtle = Turtle('star.svg', 0,45)
draw_star(turtle)
turtle.save_image()

turtle = Turtle('polygon.svg', 30,90)
draw_polygon(turtle)
turtle.save_image()