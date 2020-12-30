# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-28 23:30:58
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:36

import CustomExceptions

# function to convert decimal to binary 
def decToBinary(n): 
	
	binaryNum = [0] * n # array to store binary number
	i = 0
	while (n > 0): 
		binaryNum[i] = n % 2 	# storing remainder in binary array # 12  1100
		n = int(n / 2)
		i += 1
	binaryStr=""
	for j in range(i - 1, -1, -1): # printing binary array in reverse order 
		print(binaryNum[j], end = "")
		binaryStr+=str(binaryNum[j])
	return binaryStr

if __name__ == "__main__":
	try:	
		number = input("Enter number: ")
		if number.isnumeric() == False:
			raise CustomExceptions.ValueError(number)
		number = int(number)
		if(number <= 0 ):
			raise CustomExceptions.ValueTooSmallError(number)
		decToBinary(number)
		print(" ")
	except CustomExceptions.ValueTooSmallError:
		print("Value should be greater than 0! ")
	except CustomExceptions.ValueError:
		print("Value must be number! ")

