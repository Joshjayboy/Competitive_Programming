# Function to find the maximum number of operations
def max_operations(t, test_cases):
    # Iterate through each test case
    for case in test_cases:
        n = case[0]  # Length of the string
        s = case[1]  # The string
        max_ops = min(s.count('AB'), n - 1)
        print(max_ops)

# Input parsing
t = int(input())  # Number of test cases
test_cases = []   # List to store test cases

for _ in range(t):
    n = int(input())       # Length of the string
    s = input().strip()    # The string
    test_cases.append((n, s))

# Find and print the maximum number of operations for each test case
max_operations(t, test_cases)
