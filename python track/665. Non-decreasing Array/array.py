class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modification_count = 0

        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                modification_count += 1
                if modification_count > 1:
                    return False
                
                if index > 0 and nums[index - 1] > nums[index + 1]:
                    nums[index + 1] = nums[index]
                else:
                    nums[index] == nums[index + 1]
        
        return True