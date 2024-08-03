word = input().strip()

target = "hello"
index = 0

for char in word:
    if char == target[index]:
        index += 1
    if index == len(target):
        print("YES")
        break
else:
    print("NO")
