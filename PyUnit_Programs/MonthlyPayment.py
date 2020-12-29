# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:26
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:39


import math
import sys


# Custom Exception
class Error(Exception):
    """Base class for other exceptions"""
    pass

class IndexError(Error):
	""" Raise when all value is not entered """
	pass

class NegativeValueError(Error):
	""" Raise when value is negative """
	pass


# function monthly_payment print the payment and interest
def monthly_payment(principal, years, rate):
    r = (rate / 100) / 12   # monthly interest rate
    n = 12 * years        # number of months

    payment  = (principal * r) / (1 - math.pow(1+r, -n))
    interest = payment * n - principal

    print("Monthly payments = ",  round(payment, 2))
    print("Total interest   = ", round(interest, 2))
    return round(payment,2)

#arr = []
#for i, arg in enumerate(sys.argv):
 #   arr.append((arg))
if __name__ == '__main__':
    try:
        principal = int(input("Principal"))
        years = int(input("Years"))
        rate = int(input("Rate"))
        if(principal < 0 or years < 0 or rate < 0):
            raise NegativeValueError()
        monthly_payment(principal, years, rate)
    except NegativeValueError:
        print("Please enter non-negative value! ")
    except IndexError:
        print("Please enter all values! ")