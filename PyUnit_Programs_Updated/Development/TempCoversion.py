# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:34
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:43

import CustomExceptions

def convert_f(fahrenheit):
    cel = float(fahrenheit)
    cel = (cel*9/5)+32
    print(fahrenheit,"F to C is ",cel)
    return int(cel)


def convert_c(celsius):
    far = float(celsius)
    far = (far-32)*5/9
    print(celsius,"C to F is ",far)
    return int(far)

if __name__ == '__main__':
    try:
        fahrenheit = int(input("Enter Farhenheit : "))
        celsius = int(input("Enter Celsius: "))
        if(fahrenheit <= 0 or celsius <= 0):
            raise CustomExceptions.NegativeValueError()
        convert_f(fahrenheit)
        convert_c(celsius)
    except CustomExceptions.NegativeValueError:
        print("Enter positive numbers")
