n = int(input())
nums = list(map(int, input().split()))
# output = sorted(array)
# print(*output)
used = [False] * n  # To keep track of used elements

while not all(used):  # Repeat until all elements are used
    sequence = []
    last_num = float('-inf')  # Initialize to a very small number

    for i in range(n):
        if not used[i] and nums[i] > last_num:
            sequence.append(nums[i])
            used[i] = True
            last_num = nums[i]

    # Print the current sequence on a new line
    print(" ".join(map(str, sequence)))
