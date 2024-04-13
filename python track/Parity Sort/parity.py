def count_inversions(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def can_sort_array(arr):
    inversions = count_inversions(arr)
    if inversions % 2 == 0:
        return "YES"
    else:
        return "NO"

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_sort_array(arr))
