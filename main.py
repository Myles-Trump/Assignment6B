#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the surface area of a cylinder

import math


def surface_of_cylinder(radius_int, height_int):

    # process
    surface_area_1 = 2 * math.pi * radius_int * height_int
    surface_area_2 = 2 * math.pi * radius_int ** 2
    surface_area = surface_area_1 + surface_area_2

    # output
    print("\nYour triangle's area is {0:,.10} cm²".format(surface_area))


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    radius = input("Please input the radius (cm): ")
    height = input("Please input the height (cm): ")

    try:
        radius_int = int(radius)
        height_int = int(height)

    except Exception:
        print("\nYou have entered an invalid input.")

    finally:
        # call fucntions
        surface_of_cylinder(radius_int, height_int)


if __name__ == "__main__":
    main()
