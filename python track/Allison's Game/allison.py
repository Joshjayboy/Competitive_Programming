def largest_square_in_histogram(N, heights):
    stack = []
    max_area = 0
    i = 0

    while i < N:
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top_index = stack.pop()
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, min(heights[top_index], width) ** 2)

    while stack:
        top_index = stack.pop()
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        max_area = max(max_area, min(heights[top_index], width) ** 2)

    return max_area

# Input
N = int(input())
heights = list(map(int, input().split()))

# Output
print(largest_square_in_histogram(N, heights))
