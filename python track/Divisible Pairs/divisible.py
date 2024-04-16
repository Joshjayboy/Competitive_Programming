def count_beautiful_pairs(n, x, y, a):
    beautiful_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % x == 0 and (a[i] - a[j]) % y == 0:
                beautiful_pairs += 1

    return beautiful_pairs

# Read input
t = int(input().strip())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Calculate and output the number of beautiful pairs
    print(count_beautiful_pairs(n, x, y, a))
