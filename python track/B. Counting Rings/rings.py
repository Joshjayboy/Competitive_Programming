def max_consecutive_rings(s): # s= [OOHSSHO]
    max_count = 0
    current_count = 0

    for char in s:
        if char == 'O':
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    return max(max_count, current_count)

# Read input
s = input().strip()

# Output the result
print(max_consecutive_rings(s))
