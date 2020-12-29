# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:34
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:43
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueOutOfBoundError(Error):
	""" Raise when value is not in given bound """
	pass

class NegativeValueError(Error):
	""" Raise when value is negative """
	pass

def convert_f(fahrenheit):
    cel = float(fahrenheit)
    cel = (cel*9/5)+32
    print(fahrenheit," F to C ",cel)
    return int(cel)


def convert_c(celsius):
    far = float(celsius)
    far = (far-32)*5/9
    print(celsius," C to F ",far)
    return int(far)

#Driver Code
try:
    fahrenheit = int(input("Enter Farhenheit : "))
    celsius = int(input("Enter Celsius: "))
    if(fahrenheit <= 0 or celsius <= 0):
        raise NegativeValueError()
    convert_c(celsius)
    convert_f(fahrenheit)
except NegativeValueError:
    print("Enter positive numbers")
