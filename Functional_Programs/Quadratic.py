"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:03 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Print the roots of the equation a*x*x + b*x + c
"""

import math

# quad function to print the roots of the equation
def quad(num1, num2, num3):
    delta = num2 * num2 - 4 * num1 * num3
    print(abs(delta))
    root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
    root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
    print("root 1: ", root1)
    print("root 2 : ", root2)


try:
    number1 = int(input("Enter number 1 :"))
    number2 = int(input("Enter number 2 :"))
    number3 = int(input("Enter number 3 :"))
    if number1 <= 0 or number1 >= 1000 or number2 <= 0 or number2 >= 1000 and number3 <= 0 or number3 >= 1000:
        print("Enter number between o and 1000.")
    quad(number1, number2, number3)
except Exception:
    print("Please enter numbers in valid range.")
