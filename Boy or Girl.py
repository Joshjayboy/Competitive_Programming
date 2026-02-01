i = str(input().strip())
# print(i)

j = set(i)
# print(j)

if len(j) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")