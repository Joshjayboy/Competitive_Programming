lenght = int(input())

sequence = list(map(int, input().split()))

total = 0
for i in range(len(sequence)):
    if sequence[i] > 0:
        total += sequence[i]

if total % 2 == 0:
    print(-1) 
else:
    print(total)

