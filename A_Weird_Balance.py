for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    # print(n)
    # print(array)
    if n == 2 and array[0] == array[1]:
        print("NO")
        continue

    if sum(array[:-1]) == array[-1]:
        if array[0] != array[-1]:
            array[0], array[-1] = array[-1], array[0]
            print(' '.join(map(str, array)))

    for j in range(1, n-1):
        if sum(array[:-1]) == array[-1]:
            if array[0] != array[-1]:
                array[0], array[-1] = array[-1], array[0]
                print(' '.join(map(str, array)))
        if array[j] == array(j-1, -1, -1):
            print(array[j])
            print(sum(array[:j-1]))
            break
    #         val = array[j+1]
    #         array[j] = val
    #         array[j+1] = array[j]

    #     else:
    #         print("YES")
    #         print(array)
    #         # break
    # # print("NO")
    # for j in range(1, n):
    #     if array[j] == sum(array[:j-1]):
    #         print("NO")
