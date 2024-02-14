args = list(map(int, input().split()))
 
while args[1]:
    if args[0] % 10 == 0:
        args[0] //= 10
    else:
        args[0] -= 1
    args[1] -= 1
 
print(args[0])