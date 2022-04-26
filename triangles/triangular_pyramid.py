"""Provides a scripting component.
    Inputs:
        tri_pyr: a triangular pyramid geometry
    Output:
        points: The points that make up the image"""

__author__ = "payton"

### NOTE: May not always run on first try. Might have to try multiple times before it
### recognizes the pyramid geometry as a surface

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians, sqrt
import random as rand

def line_base_left(x, corners):
    slope = (corners[1][1] - corners[0][1])/(corners[1][0] - corners[0][0])
    y = slope*(x - corners[0][0]) + corners[0][1]
    return y

def line_base_right(x, corners):
    slope = (corners[2][1] - corners[1][1])/(corners[2][0] - corners[1][0])
    y = slope*(x - corners[1][0]) + corners[1][1]
    return y
def line_height(x, corners, point):
    point = [5, 3, math.sqrt(2)*10/2]
    midway = [(corners[0][0] + corners[1][0])/2, (corners[0][1] + corners[1][1])/2, 0]
    slope = (point[1] - midway[1])/(point[0] - midway[0])
    y = slope*(x - midway[0]) + midway[1]
    return y
    
def line(x, corners, length):
    y =  0
    if x < length/2:
        y = line_base_left(x, corners)
    elif x >= length/2:
        y = line_base_right(x, corners)
        
    return y

def rand_point(corners):
    length = 5
    rand_x = rand.uniform(0.0, length-0.2)
    y_limit = line(rand_x, corners, length)
    rand_y = rand.uniform(0.0, y_limit)
    rand_z = rand.uniform(0.0,sqrt(2)*10/2)
    return [rand_x, rand_y, rand_z]

length = 10
theta = radians(60)

first_point = [0,0,0]
second_point = [cos(theta)*length, sin(theta)*length, 0]
third_point = [length, 0, 0]
#height_point = [5, 3, sqrt(2)*10/2]
tmp_x = (first_point[0] + second_point[0] + third_point[0])/3
tmp_y = (first_point[1] + second_point[1] + third_point[1])/3
height_point = [tmp_x, tmp_y, sqrt(2)*10/2]

corners = [first_point, second_point, third_point, height_point]
triangle = rs.AddSrfPt(corners)

point = rand_point(corners)

points = [triangle]

for i in range(100000):
    valid_point = False
    
    while not valid_point:
        rhino_point = None
        random_corner = corners[rand.randrange(0,4)]
        x = (random_corner[0] + point[0])/2
        y = (random_corner[1] + point[1])/2
        z = (random_corner[2] + point[2])/2
        point = [x, y, z]
        rhino_point = rs.AddPoint(point)
        if rs.IsPointInSurface(tri_pyr, rhino_point) or rs.IsPointOnSurface(tri_pyr, rhino_point):
            points.append(rhino_point)
            valid_point = True
    valid_point = False

