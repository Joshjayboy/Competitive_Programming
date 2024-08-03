
length = int(input().strip())
array = list(map(int, input().strip().split()))


def swapssort(array):
    n = len(array)
    sorted_array = sorted(array)
    index_map = {value: i for i, value in enumerate(array)}

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or sorted_array[i] == array[i]:
            continue

        cycle_size = 0
        x = i

        while not visited[x]:
            visited[x] = True
            x = index_map[sorted_array[x]]
            cycle_size += 1

        if cycle_size > 0:
            swaps += cycle_size - 1

    return swaps


print(swapssort(array))
