for i in range(int(input())):
    t = input().strip()
    n = len(t)
    if n % 2 == 0 and t[:n//2] == t[n//2:]:
        print("YES")
    else:
        print("NO")
