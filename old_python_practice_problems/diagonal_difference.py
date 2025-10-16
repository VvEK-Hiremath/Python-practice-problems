# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter, and column=row size.
#

def diagonalDifference(arr,n):
    # Write your code here
    diag1 = 0
    diag2 = 0
    for i in range(0,n):
        diag1 += arr[i][i]
        diag2 += arr[i][n-1-i]
    return abs(diag1 - diag2)
