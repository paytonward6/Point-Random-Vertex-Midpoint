"""Provides a scripting component.
    Inputs:
        None
    Output:
        obj: the points used to make the image"""

__author__ = "payton"

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians
import random as rand

def rand_point(corners, length):
    rand_x = rand.uniform(0.0, length)
    rand_y = rand.uniform(0.0, length)
    rand_z = rand.uniform(0.0, length)
    return [rand_x, rand_y, rand_z]

scale = 2
size = 10
length = size * scale

corner_1 = [length, length, 0]
corner_2 = [0, length, 0]
corner_3 = [0,0,0]
corner_4 = [length, 0, 0]
corner_5 = [length, length, length]
corner_6 = [0, length, length]
corner_7 = [0,0,length]
corner_8 = [length, 0, length]
corners = [eval('corner_%d' %i) for i in range(1,9)]

plane = rs.WorldXYPlane()
square = rs.AddBox(corners)

point = rand_point(corners, length)

obj = []

sides = [0, length]

for i in range(100000):
    valid_point = False
    
    while not valid_point:
        rhino_point = None
        random_side_x = sides[rand.randrange(0,2)]
        random_side_y = sides[rand.randrange(0,2)]
        random_side_z = sides[rand.randrange(0,2)]
        
        x = (random_side_x + point[0])/3
        y = (random_side_y + point[1])/3
        z = (random_side_z + point[2])/3
        point = [x, y, z]
        rhino_point = rs.AddPoint(point)
        if rs.IsPointInSurface(square, rhino_point) or rs.IsPointOnSurface(square, rhino_point):
            obj.append(rhino_point)
            valid_point = True

