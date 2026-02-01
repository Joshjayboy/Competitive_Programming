n= int(input())
arr = list(map(int, input().split()))

Sereja = []
Dima = [] 

for i in range(n):
    if i % 2 == 0:
        Sereja.append(max(arr[0], arr[-1]))
        arr.remove(max(arr[0], arr[-1]))
    else:
        Dima.append(max(arr[0], arr[-1]))
        arr.remove(max(arr[0], arr[-1]))

print(sum(Sereja), sum(Dima))


