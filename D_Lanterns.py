import heapq


def max_points_from_lanterns(n, lanterns):
    lanterns.sort(key=lambda x: x[0])

    max_heap = []
    total_points = 0
    current_on_count = 0
    i = 0

    for k in range(n):
        while i < n and lanterns[i][0] <= current_on_count:
            heapq.heappush(max_heap, -lanterns[i][1])
            i += 1

        if max_heap:
            max_points = -heapq.heappop(max_heap)
            total_points += max_points
            current_on_count += 1

    return total_points


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        lanterns = []
        for _ in range(n):
            a = int(data[index])
            b = int(data[index + 1])
            lanterns.append((a, b))
            index += 2

        result = max_points_from_lanterns(n, lanterns)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
