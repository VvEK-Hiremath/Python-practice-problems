class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n):
            fl = False
            for j in range(n-i-1):
                if(arr[j] > arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    fl = True
            if(fl == False):
                break