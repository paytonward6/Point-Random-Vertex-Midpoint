"""Provides a scripting component.
    Inputs:
        divisor: slider of natural numbers
        num_points: number of points to use. best if greater than 10,000
    Output:
        points: the points used to make the image"""

__author__ = "payton"

## IF NOT USING SLIDERS, MUST INITIALIZE VARIABLES AFTER METHOD DEFINTIONS

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians, e
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

obj = []


for i in range(int(num_points)):
    random_corner = corners[rand.randrange(0,4)]
    x = (random_corner[0] + point[0])/divisor
    y = (random_corner[1] + point[1])/divisor
    point = [x, y, 0]
    rhino_point = rs.AddPoint(point)
    obj.append(rhino_point)

