"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:24 PM
   * package - com.bridgelabz.basicprograms
   * Title - Print a table of the powers of 2 that are less than or equal to 2^N
"""

try:
    number = int(input("Enter number: "))
    #print power of 2 within given range
    if number < 31:
        for num in range(1, number+1):
            print("2 ^", num, "=", 2**num)
    else:
        print("Enter number in valid range")
except Exception:
    print("Exception occured")

