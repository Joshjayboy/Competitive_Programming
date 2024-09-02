import math
no_of_ballons = int(input())

ballons = list(map(int, input().split()))

n = len(ballons)

arr = set()

for i in range(n):
    arr.add(ballons[i])
print(math.factorial(len(arr)))
