import math
a, b = map(int, input().split())
n = int(input())
result = math.gcd(a, b)
arr = []
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, y+1):
        if a % j == 0 and b % j == 0:
            arr = []
            arr.append(j)     
    if len(arr) >= 1:
        print(arr[-1])
        arr = []    
    else:
        print(-1)