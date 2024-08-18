from math import gcd
from functools import reduce

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:]))

if n == 1:
    print(max(arr))

prefix = [0] * n
prefix[0] = arr[0]
for i in range(1, n):
    prefix[i] = gcd(prefix[i-1], arr[i])

suffix = [0] * n
suffix[-1] = arr[-1]
for i in range(n-2, -1, -1):
    suffix[i] = gcd(suffix[i+1], arr[i])

maxi = 0
for i in range(n):
    if i == 0:
        current = suffix[i+1]
    elif i == n-1:
        current = prefix[i-1]
        # This is an event
    else:
        current = gcd(prefix[i-1], suffix[i+1])
    maxi = max(maxi, current)

print(maxi)
