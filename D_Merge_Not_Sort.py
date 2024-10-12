N = int(input())
c = list(map(int, input().split()))
if N == 2:
    print(-1)
output1 = []
output2 = []
if N > 2:
    for i in range(0, len(c) //2):
        output1.append(c[i])
    for i in range(N, len(c)):
        output2.append(c[i])
    print(*output1)
    print(*output2)

