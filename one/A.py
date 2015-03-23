from PIL import Image
import svgwrite
from functools import partial

def gradient():
    dimension = 255
    image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    for i in range(0,dimension):
        for j in range(0,dimension):
            image.putpixel((i,j), (i, 0, j))
    image.save("gradient.png")

def star(length = 25):
    vb = "%s, %s, %s, %s" % (-length, -length, 2*length, 2*length)
    image = svgwrite.Drawing('star.svg', width='25px', height='25px', viewBox = vb)
    line = partial(svgwrite.shapes.Line, stroke='black', stroke_width='0.1')
    group = svgwrite.container.Group()
    group.add(line((0, 0), (length - 1, 0))) #axis
    for i in range(1, length-1):
        group.add(line((i,0),(0,length - i - 1))) #bridges between axes
    for i in range(0, 4): #bit of a cheat, reusing same lines only this time they are rotated by i*90 deg
        g_c = group.copy()
        g_c.rotate(i*90)
        image.add(g_c)
    image.save()


star()
gradient()