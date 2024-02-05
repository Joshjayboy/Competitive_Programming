class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      # Use Counter to count occurrences of each letter in s and t
        s_count = Counter(s)
        t_count = Counter(t)
        
        # Compare counts and find the extra letter
        for char, count_t in t_count.items():
            if char not in s_count or count_t > s_count[char]:
                return char
