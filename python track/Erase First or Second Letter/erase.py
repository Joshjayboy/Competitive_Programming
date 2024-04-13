t = int(input()) # number of test cases
for _ in range(t):
    n = int(input()) # length of the string
    s = input() # string itself
    result = n + (n * (n - 1)) // 2
    print(result)
