from math import pi,sin, cos
from random import randrange, random
from functools import partial
import svgwrite

def cross_product(x, y):
    return x[0]*y[1]-x[1]*y[0]

def substract_points(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])

def vector_scalar_multiplication(v, s):
    return v[0]*s[0] + v[1]*s[1]

'''bool overlapping_lines defines if we consider two overlapping lines to be intersected
'''
def line_intersection(p1,p2,q1,q2, overlapping_lines=False):
    q_p = substract_points(q1, p1)  #(q - p)
    p_q = substract_points(p1, q1)  #(p - q)
    r = substract_points(p2, p1)# r
    s = substract_points(q2, q1) # s

    q_pxr = cross_product(q_p, r) # (q - p) × r
    q_pxs = cross_product(q_p, s) # (q - p) × s
    rxs = cross_product(r, s) # r × s

    if rxs:
        rxsr = 1 / rxs # 1/(r × s)
        t = q_pxs * rxsr
        u = q_pxr * rxsr 
        if (0 <= t <= 1) and (0<= u <= 1):
            return p1[0] + t*r[0], p1[1]+t*r[1] #only place to return intersection
        else:
            return None
    else:        
        if q_pxr:
            return None
        else:
            if overlapping_lines:
                return (0 <= vector_scalar_multiplication(q_p,r) <= vector_scalar_multiplication(r,r)) or (0 <= vector_scalar_multiplication(p_q, s) <= vector_scalar_multiplication(s,s))
            else:
                return None

def random_points(number_of_points, dimension):
    return [(randrange(dimension), randrange(dimension)) for i in range(number_of_points)]

def random_lines(number_of_lines, length = 75, dimension=512):
    image = svgwrite.Drawing('random_lines.svg', viewBox='0 0 %s %s' % (dimension, dimension))
    line = partial(svgwrite.shapes.Line, stroke='black')
    points = random_points(number_of_lines, dimension)
    lines = []
    for start in points:
        def target(x, y):
            angle = random()*2*pi
            return (x+length*cos(angle), y+length*sin(angle))
        while True:
            target_x, target_y = target(start[0], start[1])
            if 0<target_x<dimension and 0<target_y<dimension: #target is outside the image, lets just choose new one
                break
        image.add(line(start, (target_x, target_y)))
        lines.append((start, (target_x, target_y)))
    points = []
    for i in range(len(lines)): #simple naive approach
        for j in range(i+1, len(lines)):
            intersection = line_intersection(lines[i][0],lines[i][1], lines[j][0],lines[j][1])
            if intersection:
                image.add(svgwrite.shapes.Circle(intersection, length/20, fill='red'))
                points.append(intersection)
    image.save()
    return points

random_lines(100)