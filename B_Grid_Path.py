test_cases = int(input())
for i in range(test_cases):
    n, m, k = map(int, input().split())
    product = n * m
    val = product - 1
    if val == k:
        print("YES")
    else:
        print("NO")
