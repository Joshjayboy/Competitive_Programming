class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array = [] 
        for counter in range(n):
            shuffled_array.append(nums[counter])
            shuffled_array.append(nums[counter + n])
        
        return shuffled_array