"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:03 PM
   * package - com.bridgelabz.basicprograms
   * Title - Flip Coin and print percentage of Heads and Tails
"""


import random

heads = 0
tails = 0
heads_percent = 0
tails_percent = 0

try:
    number = int(input("Enter the times you want to Flip Coin: "))
    if number >= 0:
        for i in range(number):  # run loop n times
            coin = random.random()  # assign a value to coin either 0 or 1
            if coin < 0.5:  # if coin value is assigned as 0
                heads += 1  # increment heads
            else:  # if coin value is assigned as 1
                tails += 1  # increment tails
        heads_percent = ((heads / (heads + tails)) * 100)
        tails_percent = ((tails / (heads + tails)) * 100)
        print("Heads percent: " + str(heads_percent))s
        print("Tails percent: " + str(tails_percent))  # converting numbers to string using str()
    else:
        print("Enter the positive Number:")
except Exception:
    print("Exception occured")
