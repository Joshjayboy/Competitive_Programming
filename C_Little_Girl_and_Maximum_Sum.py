
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])

arr = list(map(int, data[2:2 + n]))

queries = []
index = 2 + n
for _ in range(q):
    li = int(data[index])
    ri = int(data[index + 1])
    queries.append((li, ri))
    index += 2

freq = [0] * (n + 1)

for l, r in queries:
    freq[l - 1] += 1
    if r < n:
        freq[r] -= 1

for i in range(1, n):
    freq[i] += freq[i - 1]

freq.pop()

freq.sort(reverse=True)
arr.sort(reverse=True)

max_sum = sum(f * a for f, a in zip(freq, arr))

print(max_sum)
