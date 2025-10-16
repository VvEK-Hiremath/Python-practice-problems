# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr,n):
    # Write your code here
    ans = [0] * 100
    for i in range(0,len(arr)):
        ans[arr[i]] += 1
    return ans
