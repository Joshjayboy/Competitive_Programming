length = int(input())
array = list(map(int, input().split()))

if length == 0:
        print(0)
    
maxlen = 1
currlen = 1

for i in range(1, length):
    if array[i] > array[i-1]:
        currlen += 1
    else:
        if currlen > maxlen:
            max_length = currlen
        currlen = 1

if currlen > maxlen:
    maxlen = currlen

print(maxlen)
