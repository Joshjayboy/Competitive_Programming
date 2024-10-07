import math

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n  # dp[i] represents the longest good sequence ending at arr[i]
    
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and math.gcd(arr[j], arr[i]) > 1:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp)) 


