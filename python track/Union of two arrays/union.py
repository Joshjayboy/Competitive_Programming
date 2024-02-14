class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        count = {}
        
        for num in A:
            count[num] = count.get(num, 0) + 1
            
        for num in B:
            remain = count.get(num, 0)
            if remain == 0:
                return 0
                
            count[num] -= 1
            
        for value in count.values():
            if value != 0:
                return 0
                
        return 1