def min_commanders_deployed(n, start_list, end_list):
    min_deployed = 0
    for i in range(n):
        if start_list[i] != end_list[i]:
            min_deployed += 1
    return min_deployed

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read inputs for each test case
    n = int(input())
    start_list = list(map(int, input().split()))
    end_list = list(map(int, input().split()))

    # Calculate and output the minimum number of commanders deployed
    print(min_commanders_deployed(n, start_list, end_list))
