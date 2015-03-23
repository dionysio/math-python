from A import random_points
import svgwrite
from functools import partial

def convex_hull(number_of_points, dimension=512):
    image = svgwrite.Drawing('convex_hull.svg', viewBox='0 0 %s %s' % (dimension, dimension))
    line = partial(svgwrite.shapes.Line, stroke='black')
    points = random_points(number_of_points, dimension)

    #jarvis algorithm
    hull_points = []
    is_on_left = lambda start, end, point: ((end[0]-start[0])*(point[1]-start[1]) - (end[1]-start[1])*(point[0]-start[0])) > 0 #checks if point is on the left side of a line(start,end)
    point_on_hull = min(points, key=lambda x: x[0]) #find first leftmost point
    i = 0
    while True:
        hull_points.append(point_on_hull)
        endpoint = points[0]
        for j in range(1, len(points)):
            if (endpoint == point_on_hull) or is_on_left(hull_points[i], endpoint, points[j]):
                endpoint = points[j]
        i += 1
        point_on_hull = endpoint
        if endpoint == hull_points[0]:
            hull_points.append(point_on_hull) #append the first point again, just so we can fully close the hull
            break

    for point in points: #draw all the points
        image.add(svgwrite.shapes.Circle(point,3))
    for i in range(len(hull_points)-1): #draw hull
        image.add(line(hull_points[i], hull_points[i+1]))
    image.save()