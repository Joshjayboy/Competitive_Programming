
def isSubset( a1, a2, n, m):
    def isSubset( a1, a2, n, m):
        a = list(a1)
        b = list(a2)
    
        for i in range(len(b)):
            
            if (b[i] not in a):
                
                return 'No'
            if (b[i] in a):
                a.remove(b[i])
                
            
        return 'Yes'
        