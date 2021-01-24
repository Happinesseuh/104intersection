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
from sources.calculations import *

def print_help():
    print("USAGE")
    print("\t./104intersection opt xp yp zp xv yv zv p\n")
    print("DESCRIPTION")
    print("\topt\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("\t(xp, yp, zp)\tcoordinates of a point by which the light ray passes through")
    print("\t(xv, yv, zv)\tcoordinates of a vector parallel to the light ray")
    print("\tp\tparameter: radius of the sphere, radius of the cylinder, orangle formed by the cone and the Z-axis")

def error_check():
    i = 1
    ac = len(argv)
    if (ac == 2 and argv[1] == "-h"):
        print_help()
        return (1)
    if (ac < 9 or ac > 9):
        return (1)
    while (i <= 8):
        for j in range(len(argv[i])):
            if ((argv[i][j] != '-') and (argv[i][j] < '0' or argv[i][j] > '9')):
                return (1)
        i += 1
    if (argv[2] == "0" and argv[3] == "0" and argv[4] == "0"):
        return (1)
    if ((argv[1] == "1" or argv[1] == "2") and int(argv[8]) <= 0):
        return (1)
    if (argv[1] == "3" and not (-90 <= int(argv[8]) <= 90)):
        return (1)

def result_intersection(argv, vector, point, radius, coefficient):
    delta = calcul_delta(coefficient[0], coefficient[1], coefficient[2])
    solution = solutions(coefficient[0], coefficient[1], coefficient[2])
    if (nb_solutions(delta) == 2):
        result1 = coordonates_point(vector, point, solution[0])
        result2 = coordonates_point(vector, point, solution[1])
        print(f"({result1[0]:.3f}, {result1[1]:.3f}, {result1[2]:.3f})")
        print(f"({result2[0]:.3f}, {result2[1]:.3f}, {result2[2]:.3f})")
    elif(nb_solutions(delta) == 1):
        result1 = coordonates_point(vector, point, solution)
        print(f"({result1[0]:.3f}, {result1[1]:.3f}, {result1[2]:.3f})")

def main():
    if (error_check() == 1):
        exit(84)
    create_point(point, int(argv[2]), int(argv[3]), int(argv[4]))
    create_vector(vector, int(argv[5]), int(argv[6]), int(argv[7]))
    radius = int(argv[8])
    if (argv[1][0] == '1'):
        sphere_header()
        coefficient = calcul_coefficient_sphere(vector, point, radius)
        result_intersection(argv, vector, point, radius, coefficient)
    elif (argv[1][0] == '2'):
        cylinder_header()
        coefficient = calcul_coefficient_cylinder(vector, point, radius)
        if (coefficient[0] == 0):
            print("There is an infinite number of intersection points.")
            return
        result_intersection(argv, vector, point, radius, coefficient)
    elif (argv[1][0] == '3'):
        cone_header()
        coefficient = calcul_coefficient_cone(vector, point, radius)
        result_intersection(argv, vector, point, radius, coefficient)

main()