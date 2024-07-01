n, m = map(int, input().split())  

matrix = [input().strip() for _ in range(n)]

def isoflag(n, m, flag):
    for row in flag:
        if len(set(row)) != 1:
            return "NO"
    for i in range(1, n):
        if matrix[i][0] == matrix[i-1][0]:
            return "NO"
    return "YES"

result = isoflag(n, m, matrix)
print(result)
