n = int(input())
limits = list(map(int, input().split()))

# Initialize the floors array with maximum limits
floors = limits[:]

# Adjust the number of floors for each skyscraper
for i in range(n):
    # Adjust to the left
    for j in range(i-1, -1, -1):
        if limits[j] > limits[i]:
            floors[i] = min(floors[i], limits[j])
        else:
            break
    # Adjust to the right
    for k in range(i+1, n):
        if limits[k] > limits[i]:
            floors[i] = min(floors[i], limits[k])
        else:
            break

# Output the resulting floors array
print(*floors)
