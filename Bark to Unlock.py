password = input().strip()
n = int(input())

one = password[0]
two = password[1]

end = False
start = False

for i in range(n):
    let = input().strip()
    if let[0] == two:
        start = True
    if let[1] == one:
        end = True
    if let == password:
        print("YES")
        exit()

print("YES" if start and end else "NO")
