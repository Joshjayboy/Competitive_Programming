n, d = map(int, input().split())

print(n, d)

s = input().strip()

print(s)
from collections import deque
queue= deque()

for i in range(n):
    if s[i] == "1":
        queue.append(i)
print(queue)

count = 0
# print(queue[1])
while queue:
    if queue[1] and queue[1] <= d:
        count += 1
        break
print(count)




# # point, length = map(int, input().split())

# # # print(point, length)


# # string =  input().strip()
# from collections import defaultdict, deque
# def min_jumps_to_reach_home(n, d, s):
#     queue = deque([(1, 0)])  # (current position, number of jumps)
#     visited = [False] * (n + 1)
#     visited[1] = True

#     while queue:
#         current_position, jumps = queue.popleft()

#         if current_position == n:
#             return jumps

#         for next_position in range(current_position + 1, min(current_position + d, n) + 1):
#             if not visited[next_position] and s[next_position - 1] == '1':
#                 visited[next_position] = True
#                 queue.append((next_position, jumps + 1))

#     return -1

# # Read input values
# n, d = map(int, input().split())
# s = input().strip()

# # Compute and print the result
# print(min_jumps_to_reach_home(n, d, s))


