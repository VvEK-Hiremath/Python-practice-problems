# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    if(len(a) == 1):
        return a[0]
    for i in range(1,len(a)):
        if(a.count(a[i]) == 1):
            return a[i]
