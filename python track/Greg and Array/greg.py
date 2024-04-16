n, m, k = map(int, input().split())
a = list(map(int, input().split()))

operations = []
for _ in range(m):
    l, r, d = map(int, input().split())
    operations.append((l, r, d))

queries = []
for _ in range(k):
    x, y = map(int, input().split())
    queries.append((x, y))

# Apply all operations to the array
for l, r, d in operations:
    for i in range(l - 1, r):
        a[i] += d

# Apply queries to the array
for x, y in queries:
    result = 0
    for i in range(x - 1, y):
        result += a[i]
    print(result, end=" ")
print()
