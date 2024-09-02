for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort(reverse = True)
    if array[0] == array[-1]:
        print("NO")
    else:
        print("YES")
        if array[0] == array[1]:
            array[0], array[-1] = array[-1], array[0]
        print(*array)