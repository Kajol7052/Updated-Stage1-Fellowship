# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2020-12-27 18:08:12
# @Last Modified by:   Your name
# @Last Modified time: 2020-12-27 18:08:12
"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:03 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Prints the Euclidean distance from the point (x, y) to the origin (0, 0)
"""
import math

# function to find euclidean distance
def distance(x1, y1):
    """
    :param x1: X value
    :param y1: Y value
    :return: print euclidean distance
    """
    diff = math.sqrt((x1 ** 2 + y1 ** 2))
    print(diff)

try:
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    if x <= 0 or x >= 1000 or y <= 0 or y >= 1000:
        print("enter the number between 0 and 1000")
        exit(1)
    distance(x, y)
except Exception:
    print("Exception occured")