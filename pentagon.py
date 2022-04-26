"""Provides a scripting component.
    Inputs:
        divisor: slider of natural numbers to divide by
        num_points: number of points to use
    Output:
        points: points used to make the image"""

__author__ = "payton"

## IF NOT USING SLIDERS, MUST INITIALIZE VARIABLES AFTER METHOD DEFINTIONS

import rhinoscriptsyntax as rs
from math import cos, sin, tan, pi, radians, sqrt
import random as rand

def line_1(x, corners):
    slope = (corners[1][1] - corners[0][1])/(corners[1][0] - corners[0][0])
    y = slope*(x - corners[0][0]) + corners[0][1]
    return y

def line_2(x, corners):
    slope = (corners[2][1] - corners[1][1])/(corners[2][0] - corners[1][0])
    y = slope*(x - corners[1][0]) + corners[1][1]
    return y
    
def line_3(x, corners):
    slope = (corners[3][1] - corners[2][1])/(corners[3][0] - corners[2][0])
    y = slope*(x - corners[2][0]) + corners[2][1]
    return y
    
def line_4(x, corners):
    slope = (corners[4][1] - corners[3][1])/(corners[4][0] - corners[3][0])
    y = slope*(x - corners[3][0]) + corners[3][1]
    return y
    
def line_5(x, corners):
    slope = (corners[4][1] - corners[0][1])/(corners[5][0] - corners[0][0])
    y = slope*(x - corners[0][0]) + corners[0][1]
    return y

def line(x, corners, length):
    y_min =  0
    y_max = 0
    if x < length/2:
        if x < corners[0][0]:
            y_min = line_1(x, corners)
        else:
            y_min = 0
        y_max = line_2(x, corners)
    elif x >= length/2:
        if x > corners[4][0]:
            y_min = line_4(x, corners)
        else:
            y_min = 0
        y_max = line_3(x, corners)
    return [y_min, y_max]

def rand_point(corners):
    length = 5
    rand_x = rand.uniform(corners[1][0], corners[3][0])
    y_limit = line(rand_x, corners, length - 1)
    rand_y = rand.uniform(y_limit[0] + 1, y_limit[1] - 1)
    return [rand_x, rand_y, 0]

length =10
theta = radians(108)
theta_prime = radians(180 - 108)
point_1 = [0,0,0]
point_2 = [cos(theta)*length, sin(theta)*length, 0]
point_5 = [length, 0, 0]
point_4 = [cos(theta_prime)*length + point_5[0], sin(theta_prime)*length, 0]

tmp = [(point_1[0] + point_4[0])/2, (point_1[1] + point_4[1])/2, 0]
tmp = sqrt((tmp[0] - point_5[0])**2 + (tmp[1] - point_5[1])**2)

point_3 = [(point_5[0] + point_1[0])/2,tmp + point_2[1], 0]

corners = [eval("point_%d" %i) for i in range(1,6)]

pentagon = rs.AddSrfPt(corners)
point = rand_point(corners)

points = [point]

for i in range(int(num_points)):
    random_corner = corners[rand.randrange(0,5)]
    x = (random_corner[0] + point[0])/divisor
    y = (random_corner[1] + point[1])/divisor
    point = [x, y, 0]
    rhino_point = rs.AddPoint(point)
    points.append(rhino_point)

