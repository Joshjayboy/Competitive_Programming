n, k = map(int, input().split())  # Input n and k
heights = list(map(int, input().split()))  # Input heights of planks

# Initialize variables to keep track of the minimum sum and its starting index
min_sum = float('inf')
start_index = 0

# Calculate the sum of the first k planks
current_sum = sum(heights[:k])

# Iterate through the rest of the planks
for i in range(n - k + 1):
    # Update minimum sum and starting index if current sum is smaller
    if current_sum < min_sum:
        min_sum = current_sum
        start_index = i
    
    # Slide the window by removing the first plank and adding the next plank
    current_sum = current_sum - heights[i] + heights[i + k]

# Output the starting index of the consecutive k planks with minimum total height
print(start_index + 1)  # Adding 1 to convert zero-based index to one-based index
