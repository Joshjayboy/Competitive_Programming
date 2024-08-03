integer = int(input())

array = list(map(int, input().split()))
array.sort()
# print(array)
half = len(array) // 2

firstHalf = []
secondHalf = []

for i in range(0, half):
    firstHalf.append(array[i])

for j in range(half, 2*integer):
    secondHalf.append(array[j])


if sum(firstHalf) != sum(secondHalf):   
    print(_ for _ in range(0, len(firstHalf)))
else:
    print(-1)

