#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-MAT-100-PAR-1-1-104intersection-ines.maaroufi
## File description:
## class
##

from math import *
from sys import *
from sources.class_create import *

def sphere_header():
    print(f'Sphere of radius {argv[8]}')
    print("Line passing through the point ", end = '')
    print(f'({argv[2]}, {argv[3]}, {argv[4]}) ', end = '') 
    print(f'and parallel to the vector ({argv[5]}, {argv[6]}, {argv[7]})')

def calcul_coefficient_sphere(vector, point, radius):
    a = (pow(vector.x1, 2) + pow(vector.y1, 2) + pow(vector.z1, 2))
    b = 2 * ((point.x2 * vector.x1) + (point.y2 * vector.y1) + (point.z2 * vector.z1))
    c = pow(point.x2, 2) + pow(point.y2, 2) + pow(point.z2, 2) - pow(radius, 2)
    return(a, b, c)