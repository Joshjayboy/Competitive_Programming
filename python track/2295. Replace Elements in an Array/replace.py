class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexes_hash = {}

        for index, num in enumerate(nums):
            indexes_hash[num] = index
        
        for operation in operations:
            nums[indexes_hash[operation[0]]] = operation[1]
            indexes_hash[operation[1]] = indexes_hash[operation[0]]
            del indexes_hash[operation[0]]
        
        return nums 