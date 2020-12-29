# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:14
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:40

import math


# Custom Exception
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueError(Error):
	""" Raise when value is not a number """
	pass

class NegativeValueError(Error):
	""" Raise when value is negative """
	pass

class SquareRooter:

# sqrt function to print square root of a number using newton's formula
  def sqrt(self,c):
      t = c
      epsilon = 1e-15 
      while (math.fabs(t - c/t) > epsilon*t):
          t = (c/t + t) / 2.0
      print("Square root is: ", round(t,2))
      return int(round(t,2))

if __name__ == '__main__':
  try:
    number = int(input("Enter number: "))
    if(number < 0):
      raise NegativeValueError(number)
    caller = SquareRooter()
    caller.sqrt(number)
  except NegativeValueError:
    print("Please enter non-negative number! ")











#public class SqrtNewtonMethod {
 #   public static void main(String[] args) {
  #      double c = Double.parseDouble(args[0]);
#
 #       double epsilon = 1e-15;    // relative error tolerance
  #      double t = c;              // estimate of the square root of c

    #    // repeatedly apply Newton update step until desired precision is achieved
   #     while (Math.abs(t - c/t) > epsilon*t) {
     #       t = (c/t + t) / 2.0;
      #  }
       ##System.out.println(t);
    #}
#}