number = int(input())
array = list(map(int, input().split()))

arr = []
length = 0

for i in range(0, number-1):
    if array[i] > 1:  # 2 > 1
        arr.append(array[i])  # append 2
        if array[i+1] > array[i] + 1:
            arr.append(array[i+1])

p = len(arr) // 2
# print(len(arr)//2)
if p % 2 == 0:
    print(p)
else:
    print(p + 1)
