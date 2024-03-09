def max_total_difference(n, m, frodo_list, sam_list):
    frodo_list.sort()
    sam_list.sort(reverse=True)
    
    selected_numbers = set()
    total_difference = 0
    
    for num in sam_list:
        if len(selected_numbers) == n:
            break
        if num not in frodo_list:
            selected_numbers.add(num)
    
    for i in range(n):
        total_difference += abs(frodo_list[i] - selected_numbers.pop())
    
    return total_difference

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read inputs for each test case
    n, m = map(int, input().split())
    frodo_list = list(map(int, input().split()))
    sam_list = list(map(int, input().split()))

    # Output the maximum total difference
    print(max_total_difference(n, m, frodo_list, sam_list))
