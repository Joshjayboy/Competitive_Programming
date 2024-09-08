n = int(input())
p = list(map(int, input().split()))

tree = 0
for i in range(0, n):
    if p[i] == i + 1:
        tree += 1

print(tree)
