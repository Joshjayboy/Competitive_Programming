
input = input().strip()
stack = []
valid = [False] * len(input)

for i, char in enumerate(input):
    if char == '(':
        stack.append(i)
    elif char == ')':
        if stack:
            open = stack.pop()
            valid[open] = True
            valid[i] = True

maxl = 0
currentl = 0

for v in valid:
    if v:
        currentl += 1
        maxl = max(maxl, currentl)
    else:
        currentl = 0

print(maxl)
