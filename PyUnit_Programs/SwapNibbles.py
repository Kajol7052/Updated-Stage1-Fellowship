# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2020-12-29 22:19:34
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2020-12-29 22:28:41


def decToBinary(n): 
	return ((n & 0x0F)<<4 | (n & 0xF0)>>4)


if __name__ == "__main__":
	num = int(input("Enter number: "))
	print(decToBinary(num))
	