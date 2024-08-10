
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

prefixSum = 0
prefixCounts = {0: 1}
count = 0

for i in range(N):
    prefixSum += A[i]
    mod_value = prefixSum % M

    if mod_value in prefixCounts:
        count += prefixCounts[mod_value]
        prefixCounts[mod_value] += 1
    else:
        prefixCounts[mod_value] = 1

print(count)
