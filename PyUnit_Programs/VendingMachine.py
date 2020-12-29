# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:29:13
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:53

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueError(Error):
	""" Raise when value is not a number """
	pass

class ValueTooSmallError(Error):
	""" Raise when value is less then or equal to 0 """
	pass

# Function to count and print currency notes 
def countCurrency(amount): 
	
	notes = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] 
	noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
	
	print ("Currency Count -> ") 
	res=""
	for i, j in zip(notes, noteCounter): 
		if amount >= i: 	# amount=677
			j = amount // i 	# j=677//500	= 1
			amount = amount - j * i 	# amount=677-1*500	=177 
			print (i ," : ", j) 		# 500 : 1
			res+=str(i)+":"+str(j)+","
	print(res)
	return res
try:
	amount = input("Enter the amount: ")
	if amount.isnumeric() == False:
		raise ValueError(amount)
	amount = int(amount)
	if(amount <= 0 ):
		raise ValueTooSmallError(amount)
	countCurrency(amount)
except ValueTooSmallError:
	print("Value should be greater than 0! ")
except ValueError:
	print("Value must be number! ")
