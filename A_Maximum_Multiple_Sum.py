testcases = int(input())
for i in range(testcases):
    n = int(input())
    msum = 0
    best = 2

    for x in range(2, n + 1):
        k = n // x
        current = x * (k * (k + 1)) // 2

        if current > msum:
            msum = current
            best = x
    print(best)
