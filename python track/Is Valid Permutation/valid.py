def is_permutation_possible(n, prefix_sums):
    expected_sum = (n * (n + 1)) // 2
    prefix_sum_diff = [prefix_sums[0]]
    
    for i in range(1, n-1):
        prefix_sum_diff.append(prefix_sums[i] - prefix_sums[i-1])
    
    prefix_sum_diff.append(expected_sum - prefix_sums[-1])
    
    if sorted(prefix_sum_diff) == list(range(1, n+1)):
        return "YES"
    else:
        return "NO"

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    prefix_sums = list(map(int, input().split()))
    print(is_permutation_possible(n, prefix_sums))
