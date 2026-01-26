t = int(input().strip())

for _ in range(t):
    expr = input().strip()
    a, b = expr.split('+')
    print(int(a) + int(b))
