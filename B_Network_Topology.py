from collections import defaultdict

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

diction = defaultdict(int)

for i, j in edges:
    diction[i] += 1
    diction[j] += 1

occurence = defaultdict(int)

for k in range(1, n+1):
    occurence[diction[k]] += 1

if occurence[1] == 2 and occurence[2] == n-2:
    print("bus topology")


elif occurence[2] == n:
    print("ring topology")

elif occurence[n-1] == 1 and occurence[1] == n-1:
    print("star topology")

else:
    print("unknown topology")
