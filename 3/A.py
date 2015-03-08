from math import radians, cos, sin
import svgwrite 
from functools import partial

class Turtle():
    def __init__(self, filename = 'turtle.svg'):
        if filename:
            self.clear_image(filename)

    def clear_image(self, filename = 'turtle.svg'):
        self.x = 255
        self.y = 255
        self.angle = 0.0
        self.draw = True
        self.image = svgwrite.Drawing(filename, viewBox="0,0,512,512")
        self.line = partial(svgwrite.shapes.Line, stroke='black')
        self.points = []

    def penup(self):
        self.draw = False

    def current_position(self):
        return self.x, self.y

    def pendown(self):
        self.draw = True

    def _draw_line_abs(self, xy, target_xy):
        self.image.add(self.line(xy, target_xy))

    def _draw_line(self, target_x, target_y):
        self.image.add(self.line((self.x, self.y), (target_x, target_y)))

    def save_image(self):
        self.image.save()

    def back(self, step):
        self.forward(-step)

    def forward(self, step):
        self.points.append((self.x, self.y))
        new_x, new_y = self.move(self.x, self.y, step, self.angle)
        self.x += new_x
        self.y += new_y

    def move(self, from_x, from_y, step, angle):
        rad = radians(angle)
        new_x   = step * cos(rad)
        new_y   = step * sin(rad)
        if self.draw:            
            self._draw_line(from_x+new_x, from_y+new_y)
        return new_x, new_y

    def right(self, angle):
        self.change_angle((self.angle + angle) % 360)

    def left(self, angle):
        self.change_angle((self.angle - angle) % 360)

    def change_angle(self, angle):
        self.angle = angle


def draw_polygon(turtle, number_of_vertices, length=25):
    angle = 360.0/number_of_vertices
    for i in range(number_of_vertices):
        turtle.forward(length)
        turtle.left(angle)

def draw_star(turtle, number_of_vertices, length=100):
    angle = 180.0 - 180.0 / number_of_vertices
    for i in range(number_of_vertices):
        turtle.forward(length)
        turtle.right(angle)

turtle = Turtle('star.svg')
draw_star(turtle, 9)
turtle.save_image()

turtle = Turtle('polygon.svg')
draw_polygon(turtle, 6)
turtle.save_image()

