class Solution: 
    def select(self, arr, i,n):
        mn = i
        for i in range(i,n):
            if(arr[mn]>arr[i]):
                mn = i
        return mn
    
    def selectionSort(self, arr,n):
        for i in range(0,n):
            sm = self.select(arr,i,n);
            arr[i],arr[sm] = arr[sm],arr[i]
        
        return arr