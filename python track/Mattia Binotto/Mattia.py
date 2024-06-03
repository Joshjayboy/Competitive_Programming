def max_satisfied_drivers(n, times):
    times.sort()  # Sort the pit stop times in ascending order
    max_satisfied = 0
    for i in range(n):
        if times[i] <= i + 1:  # Check if the current driver's pit stop time is less than or equal to their position in the queue
            max_satisfied += 1
    return max_satisfied

# Example usage:
n = 5
times = [15, 2, 1, 5, 3]
result = max_satisfied_drivers(n, times)
print(result)
