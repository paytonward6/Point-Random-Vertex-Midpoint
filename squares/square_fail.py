"""Provides a scripting component.
    Inputs:
        None
    Output:
        points: the points that make up the image"""

__author__ = "payton"


## Fails due to the divisor being 2

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians
import random as rand

def rand_point(corners, length):
    rand_x = rand.uniform(0.0, length)
    rand_y = rand.uniform(0.0, length)
    return [rand_x, rand_y, 0]

length = 10

corner_1 = [length, length, 0]
corner_2 = [0, length, 0]
corner_3 = [0,0,0]
corner_4 = [length, 0, 0]
corners = [corner_1, corner_2, corner_3, corner_4]

plane = rs.WorldXYPlane()
square = rs.AddPlaneSurface(plane, length, length)

point = rand_point(corners, length)

test = rs.AddPoint(point)
obj = []


for i in range(10000):
    random_corner = corners[rand.randrange(0,4)]
    x = (random_corner[0] + point[0])/2
    y = (random_corner[1] + point[1])/2
    point = [x, y, 0]
    rhino_point = rs.AddPoint(point)
    obj.append(rhino_point)

