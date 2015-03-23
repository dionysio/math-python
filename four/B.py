from PIL import Image

dimension = 200

def cross_product(x, y):
    return x[0]*y[1]-x[1]*y[0]

def substract_points(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])

def vector_scalar_multiplication(v, s):
    return v[0]*s[0] + v[1]*s[1]
'''http://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
we want to solve:
t = (q − p) × s / (r × s) and u = (q − p) × r / (r × s)
and there are five cases:

1. If r × s = 0 and (q − p) × r = 0, then the two lines are collinear. If in addition, either 0 ≤ (q − p) · r ≤ r · r or 0 ≤ (p − q) · s ≤ s · s, then the two lines are overlapping.

2. If r × s = 0 and (q − p) × r = 0, but neither 0 ≤ (q − p) · r ≤ r · r nor 0 ≤ (p − q) · s ≤ s · s, then the two lines are collinear but disjoint.

3. If r × s = 0 and (q − p) × r ≠ 0, then the two lines are parallel and non-intersecting.

4. If r × s ≠ 0 and 0 ≤ t ≤ 1 and 0 ≤ u ≤ 1, the two line segments meet at the point p + t r = q + u s.

5. Otherwise, the two line segments are not parallel but do not intersect.
'''
def are_intersected(p1,p2,q1,q2):
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
            return (0 <= vector_scalar_multiplication(q_p,r) <= vector_scalar_multiplication(r,r)) or (0 <= vector_scalar_multiplication(p_q, s) <= vector_scalar_multiplication(s,s)) #1. and 2. case
'''
'''
def polygon(vertices, image=None, color_func=None):
    if not image:
        image = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    if not color_func:
        color_func = lambda x,y: (0,0,0)
    vertices.append(vertices[0])
    for i in range(dimension):
        for j in range(dimension):
            base_point = (i,j)
            counter = 0
            for position in range(len(vertices)-1):
                counter += are_intersected(base_point, (dimension, dimension), vertices[position], vertices[position+1])
            if counter % 2:
                color = color_func(i,j)
                image.putpixel(base_point, color)
    image = image.transpose(Image.TRANSPOSE)
    image = image.transpose(Image.ROTATE_90)
    return image

polygon([(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)]).save('polygon.png')