from A import random_points
import svgwrite
from itertools import combinations, permutations
from functools import partial

def cross_product(x, y):
    return x[0]*y[1]-x[1]*y[0]

def substract_points(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])

def vector_scalar_multiplication(v, s):
    return v[0]*s[0] + v[1]*s[1]

def are_intersected(p1,p2,q1,q2):
    if p1==q1 or q1==q2:
        return False
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
        return (0 <= t <= 1) and (0<= u <= 1) #4. case    
    else:        
        if q_pxr:
            return False #3. case
        else:
            return False
            #return (0 <= vector_scalar_multiplication(q_p,r) <= vector_scalar_multiplication(r,r)) or (0 <= vector_scalar_multiplication(p_q, s) <= vector_scalar_multiplication(s,s)) #1. and 2. case

def triangulation(number_of_points, dimension=512):
    image = svgwrite.Drawing('triangulation.svg', viewBox='0 0 %s %s' % (dimension, dimension))
    line = partial(svgwrite.shapes.Line, stroke='black')
    points = random_points(number_of_points, dimension)
    combos = list(permutations(points,2)) #I will be reusing the same combos over and over
    result = set()
    for p in combos:
        for q in result:
            #if p[0]!=q[0] and p[1]!=q[1]:
            if are_intersected(p[0],p[1],q[0],q[1]):
                break
        else:
            result.add(p)
    print(result)
    for start, end in result:
        image.add(line(start, end))
    image.save()