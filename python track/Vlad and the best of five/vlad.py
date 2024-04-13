# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the string
    s = input()
    
    # Count occurrences of 'A' and 'B'
    count_a = s.count('A')
    count_b = s.count('B')
    
    # Output the letter that appears most frequently
    if count_a > count_b:
        print('A')
    elif count_b > count_a:
        print('B')
    else:
        # If both 'A' and 'B' appear the same number of times, output any one of them
        print('A')  # You can choose 'B' as well, as they are equal
