from collections import deque
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append(grid)


def bfs(grid, visited, start):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    volume = 0

    while queue:
        x, y = queue.popleft()
        volume += grid[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return volume


def largest(test_cases):
    results = []

    for grid in test_cases:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        max_volume = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visited[i][j]:
                    volume = bfs(grid, visited, (i, j))
                    max_volume = max(max_volume, volume)

        results.append(max_volume)

    return results


results = largest(test_cases)


for result in results:
    print(result)
