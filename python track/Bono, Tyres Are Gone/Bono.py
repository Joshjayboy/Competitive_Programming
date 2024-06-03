n = int(input())
commands = [input().split() for _ in range(2 * n)]

stack = []
reorders = 0

for cmd, arg in commands:
    if cmd == "add":
        stack.append(int(arg))
    else:  # remove
        if stack and stack[-1] == int(arg):
            stack.pop()
        else:
            reorders += 1
            stack = []

print(reorders)
