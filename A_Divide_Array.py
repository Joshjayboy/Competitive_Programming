def partition_array(n, arr):
    negative = []
    positive = []
    zeroes = []
    
    # Categorize numbers
    for number in arr:
        if number < 0:
            negative.append(number)
        elif number > 0:
            positive.append(number)
        else:
            zeroes.append(number)
    
    # Check that we can make the partitions
    if len(negative) == 0 or len(positive) == 0 or len(zeroes) == 0:
        raise ValueError("It's guaranteed that a solution exists, but categorization failed.")
    
    # First partition: product < 0 (at least one negative number)
    first_partition = [negative.pop()]
    
    # Second partition: product > 0 (at least one positive number)
    second_partition = [positive.pop()]
    
    # Third partition: product = 0 (all zeroes)
    third_partition = zeroes
    
    # Add remaining numbers to partitions
    if negative:
        first_partition.extend(negative)
    if positive:
        second_partition.extend(positive)
    
    # Print results
    print(len(first_partition), ' '.join(map(str, first_partition)))
    print(len(second_partition), ' '.join(map(str, second_partition)))
    print(len(third_partition), ' '.join(map(str, third_partition)))

# Example usage
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:]))

partition_array(n, arr)




# length_of_array = int(input())
# array = list(map(int, input().split()))
# from functools import reduce

# set1 = []
# product = reduce(lambda x, y: x * y, set1)
# print(product)
# set2 = []
# set3 = []



# for i in range(length_of_array):
#     if array[i] < 0:
#         set1.append(array[i])
#     if array[i] > 0:
#         set2.append(array[1])
#     if array[i] == 0:
#         set3.append(array[i])

# one = ''.join(map(str, set1))
# two = ''.join(map(str, set2))
# three = ''.join(map(str, set3))

# print(len(set1), one)
# print(len(set2), two)
# print(len(set3), three)
