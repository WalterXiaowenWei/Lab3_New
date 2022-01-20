#3) Write a program to calculate the volume of a cylinder. Start with a variable that contains the diameter of the end of the circle, and another variable that references the height in meters.

import math
from unittest.loader import VALID_MODULE_NAME

def volume(diameter, height):
    pi = math.pi
    volume = pi * (0.5 * diameter)**2*height
    return volume

x = 2
while x < 3:
    diameter = float(input("Please input the diameter in meters of the end of the circle for the cylinder: "))
    height = float(input("Please input the height in meters for the cylinder: "))
    print("The volume of the cylinder is ", volume(diameter, height), "cubic meters")