"""
   * author - kajol
   * date - 12/25/2020
   * time - 10:30 AM
   * package - com.bridgelabz.logicalprograms34
   * Title - Generate random number and to process distinct coupons.
"""

import numpy as np


class CouponsProgram:

    # coupons function is to generate distinct coupon numberss
    def coupons(self, number):
        """
            :param number: no of coupons wants to print
            :return:
        """
        array = []
        counter = 0
        while True:
            rand = np.random.randint(10, 100)
            array.append(rand)
            unique = set(array)
            counter += 1
            print(list(unique))
            if len(unique) == number:
                break
        print("Total number of random numbers generated : ", counter)


if __name__ == '__main__':
    try:
        numbers = int(input("How many coupons you want to generate ??"))
        if numbers <= 1 or numbers >= 1000:
            print("Please enter the number between 0 and 1000")
        caller = CouponsProgram()
        caller.coupons(numbers)
    except ValueError:
        print("Enter valid input")
