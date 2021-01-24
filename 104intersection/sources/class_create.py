#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-MAT-100-PAR-1-1-104intersection-ines.maaroufi
## File description:
## class
##

from math import *
from sys import *

class vector:
    def __init__(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

class point:
    def __init__(self, x2, y2, z2):
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

def create_point(point, x, y, z):
    point.x2 = x
    point.y2 = y
    point.z2 = z

def create_vector(vector, x, y, z):
    vector.x1 = x
    vector.y1 = y
    vector.z1 = z