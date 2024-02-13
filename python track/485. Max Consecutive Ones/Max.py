class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       max_sequence_count = 0
       current_sequence_count = 0
       found_zero = False

       for num in nums:
            if num == 0 and not found_zero:
                found_zero = True
                if current_sequence_count > max_sequence_count:
                    max_sequence_count = current_sequence_count
                current_sequence_count = 0
            elif num == 1:
                found_zero = False
                current_sequence_count += 1

       return max(max_sequence_count, current_sequence_count)