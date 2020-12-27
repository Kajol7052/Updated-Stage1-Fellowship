
"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:21 PM
   * package - com.bridgelabz.basicprograms
   * Title - Determine Leap Year or not
"""
try:
    year = int(input("Enter the Year Number: "))
    count = 0
    tempYear = year
    # Check if number of digits in a year is equal to 4 or not.
    while tempYear > 0:
        count += 1
        tempYear = tempYear // 10
    if count != 4:
        print("Not a valid year")
        exit(1)
    # Leap Year logic
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print("%d is a Leap Year" % year)
    else:
        print("%d is Not the Leap Year" % year)
except Exception:
    print("Exception occured")