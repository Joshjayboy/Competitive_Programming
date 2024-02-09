class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]

        result = []
        # Alternate between adding positive and negative integers
        while positives and negatives:
            result.append(positives.pop(0))
            result.append(negatives.pop(0))

        # Append the remaining elements if any
        result.extend(positives)
        result.extend(negatives)

        # Ensure the first element is positive
        if result[0] < 0:
            # Find the first positive integer and bring it to the front
            for i in range(len(result)):
                if result[i] > 0:
                    result.insert(0, result.pop(i))
                    break

        return result