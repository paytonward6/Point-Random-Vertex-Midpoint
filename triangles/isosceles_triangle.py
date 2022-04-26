"""Provides a scripting component.
    Inputs:
        None
    Output:
        points: The points that make up the image"""

__author__ = "payton"

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians
import random as rand

def line_left(x, corners):
    slope = (corners[1][1] - corners[0][1])/(corners[1][0] - corners[0][0])
    y = slope*(x - corners[0][0]) + corners[0][1]
    return y

def line_right(x, corners):
    slope = (corners[2][1] - corners[1][1])/(corners[2][0] - corners[1][0])
    y = slope*(x - corners[1][0]) + corners[1][1]
    return y

def line(x, corners, length):
    y =  0
    if x < length/2:
        y = line_left(x, corners)
    elif x >= length/2:
        y = line_right(x, corners)
        
    return y

def rand_point(corners):
    length = 5
    rand_x = rand.uniform(0.0, length-0.2)
    y_limit = line(rand_x, corners, length)
    rand_y = rand.uniform(0.0, y_limit)
    return [rand_x, rand_y, 0]

length = 10
theta = radians(60)
first_point = [0,0,0]
second_point = [cos(theta)*length, sin(theta)*(length + 10), 0]
third_point = [length, 0, 0]

corners = [first_point, second_point, third_point]
triangle = rs.AddSrfPt(corners)
print(rs.SurfaceArea(triangle))
point = rand_point(corners)

test = rs.AddPoint(point)
points = [triangle, test]

for i in range(100000):
    random_corner = corners[rand.randrange(0,3)]
    x = (random_corner[0] + point[0])/2
    y = (random_corner[1] + point[1])/2
    point = [x, y, 0]
    rhino_point = rs.AddPoint(point)
    points.append(rhino_point)

