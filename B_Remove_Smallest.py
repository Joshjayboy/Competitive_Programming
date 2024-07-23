
t = int(input())
def reduce(n, a):
    if n == 1:
        return "YES"
    a.sort()
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            return "NO"
    return "YES"


results = []
for _ in range(t):
    n = int(input())
    a = list(int(x) for x in input().split())
    result = reduce(n, a)
    results.append(result)

for result in results:
    print(result)

