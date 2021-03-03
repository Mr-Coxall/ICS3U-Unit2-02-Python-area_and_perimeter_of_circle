#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program calculates the area and perimeter of a circle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a circle

    # input
    radius = int(input("Enter radius of a circle (mm): "))

    # process
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    # output
    print("")
    print("Area is {0}mm².".format(area))
    print("Perimeter is {0}mm.".format(perimeter))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
