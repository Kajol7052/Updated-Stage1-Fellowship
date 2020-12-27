"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:02 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Print 2 Dimensional array
"""

# function to print 2D array
def array_2d(row, col):
    """
    :param row: denotes number of rows
    :param col: denotes number of columns
    :return:
    """
    array = []
    for row_num in range(row):
        temp_array = []
        for col_num in range(col):
            number = int(input("Enter any number: "))
            temp_array.append(number)
        array.append(temp_array)
    print(array)

try:
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of cols: "))
    if row <= 0 or row >= 100 or col <= 0 or col >= 100:
        print("Enter valid input within range.")
    array_2d(row, col)
except Exception:
    print("Exception occured")