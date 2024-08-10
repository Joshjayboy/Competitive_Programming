import sys


def max_good_subrectangle(n, m, matrix):
    # Step 1: Compute prefix sums for each column
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + \
                (1 if matrix[i - 1][j - 1] == '1' else 0)

    max_area = 0

    # Step 2: Iterate over pairs of rows
    for top in range(1, n + 1):
        for bottom in range(top, n + 1):
            count = [0] * (m + 1)

            for col in range(1, m + 1):
                count[col] = prefix_sum[bottom][col] - prefix_sum[top - 1][col]

            # Step 3: Use hashmap to find the longest subarray with the target sum
            prefix_col_sum = 0
            seen = {0: 0}

            for col in range(1, m + 1):
                prefix_col_sum += count[col]
                target = prefix_col_sum - (bottom - top + 1)

                if target in seen:
                    left_col = seen[target]
                    width = col - left_col
                    height = bottom - top + 1
                    area = width * height
                    max_area = max(max_area, area)

                if prefix_col_sum not in seen:
                    seen[prefix_col_sum] = col

    return max_area


# Input reading
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
matrix = [data[i * m + 2:(i + 1) * m + 2] for i in range(n)]

# Output result
print(max_good_subrectangle(n, m, matrix))
