for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    ans = 0
    maxi = 0
    while i < n and a[i] <= s:
        s -= a[i]
        if a[i] > maxi:
            maxi = a[i]
            ans = i
        i += 1
    if i < n:
        if a[i] > maxi:
            print(i+1)
        else:
            print(ans+1)
    else:
        print(0)
