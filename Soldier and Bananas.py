k, n, w = map(int, input().split())

arr=[]

for i in range(w+1):
    arr.append(i * k)
    i+1
    
add = sum(arr)

if (add-n) > 0:
    print((add - n))
else:
    print("0")
