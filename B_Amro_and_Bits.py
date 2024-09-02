for i in range(int(input())):
    x = int(input())
    if x == 1:
         y = 3
    elif x & (x-1) == 0:
         y= x+1
    else:
         y= x & -x

    print(y)
