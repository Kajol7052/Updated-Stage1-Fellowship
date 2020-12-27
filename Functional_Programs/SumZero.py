"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:02 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Read in N integers and counts the number of triples that sum to exactly 0.
"""

# function to find different triplets 
def find_triplets(arr, n):
    """
    :param arr: containing all the elements
    :param n: number of elements
    :return: triplets that sum adds to 0
    """
    found = True
    count = 0
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    found = True
                    count = count + 1
    print("The number of triplets is: ", count)

    # If no triplet with 0 sum found in array
    if not found:
        print(" not exist ")


while True:
    try:
        array = []
        length = int(input("Enter length of array: "))
        for i in range(length):
            temp = int(input("Enter numbers: "))
            array.append(temp)
        find_triplets(array, length)
        break
    except Exception:
        print("Check the input")
