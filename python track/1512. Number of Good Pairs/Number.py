class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
          # Use Counter to count occurrences of each number
        num_count = Counter(nums)
        
        # Initialize the total count of good pairs
        good_pairs = 0
        
        # Calculate good pairs for each number
        for count in num_count.values():
            good_pairs += count * (count - 1) // 2
        
        return good_pairs