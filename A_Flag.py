# n, m = map(int, input().split())  
x = input()
t = x.split()
n = int(t[0])
m = int(t[1])
# print("this is n", n)
# print("this is m", m)
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
