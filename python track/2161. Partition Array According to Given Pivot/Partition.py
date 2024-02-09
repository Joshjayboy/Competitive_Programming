class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # creat 3 lisst to accomodate numbers >, < and = to the pivot number
        list1 = []
        list2 = []
        list3 = []

        # iterate nums and append results to the list
        for i in nums:
            if i < pivot:
                list1.append(i)
            elif i == pivot:
                list2.append(i)
            elif i > pivot:
                list3.append(i)

        # Put the list together
        return (list1 + list2 + list3) 
        
                

        
