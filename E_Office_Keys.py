n, k, office = map(int, input().split())
people = list(map(int, input().split()))
keys = list(map(int, input().split()))

people.sort()
keys.sort()

low, high = 0, 10**9
while low < high:
    mid = (low + high) // 2
    for i in range(len(keys) - n + 1):
        j = 0
        while j < n and abs(people[j] - keys[i + j]) + abs(keys[i + j] - office) <= k:
            j += 1
        if j == n:
            print(True)
        else:
            low = mid + 1
    high = mid

print(low)
