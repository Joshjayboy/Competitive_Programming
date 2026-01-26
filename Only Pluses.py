t = int(input().strip())
arr= []
for i in range(t):
    a, b, c = map(int, input().strip().split())
    print((a+b) * (b+a) * c)
    