#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-MAT-100-PAR-1-1-104intersection-ines.maaroufi
## File description:
## main
##

from math import *
from sys import *
from sources.class_create import *
from sources.cone import *
from sources.sphere import *
from sources.cylinder import *

def calcul_delta(a, b, c):
    delta = pow(b, 2) - (4 * a *c)
    return delta

def nb_solutions(delta):
    if (delta > 0):
        return (2)
    elif (delta == 0):
        return (1)
    else:
        return (0)

def solutions(a, b, c):
    delta = calcul_delta(a, b, c)
    if (delta > 0):
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("2 intersection points:")
        return (x1, x2)
    elif (delta == 0):
        x0 = -b / (2 * a)
        print("1 intersection point:")
        return (x0)
    else:
        print("No intersection point.")
        return

def calcul_coefficient(vector, point, radius):
    a = (pow(vector.x1, 2) + pow(vector.y1, 2) + pow(vector.z1, 2))
    b = 2 * ((point.x2 * vector.x1) + (point.y2 * vector.y1) + (point.z2 * vector.z1))
    c = pow(point.x2, 2) + pow(point.y2, 2) + pow(point.z2, 2) - pow(radius, 2)
    return(a, b, c)

def coordonates_point(vector, point, t):
    xt = point.x2 + (t * vector.x1)
    yt = point.y2 + (t * vector.y1)
    zt = point.z2 + (t * vector.z1)
    return (xt, yt, zt)                                                                                                                                                                                                                                                                                                                       
