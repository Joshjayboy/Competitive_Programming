import sys
input = sys.stdin.read
data = input().split()

s = data[0]
n = len(s)

m = int(data[1])

queries = []
index = 2
for _ in range(m):
    li = int(data[index])
    ri = int(data[index + 1])
    queries.append((li, ri))
    index += 2

prefix = [0] * n

for i in range(1, n):
    prefix[i] = prefix[i - 1]
    if s[i] == s[i - 1]:
        prefix[i] += 1        

results = []
for li, ri in queries:
    li -= 1
    ri -= 1
    result = prefix[ri] - prefix[li]
    results.append(result)

for result in results:
    print(result)
