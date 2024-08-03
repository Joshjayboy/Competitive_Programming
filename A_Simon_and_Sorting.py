import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []


def abc(s):
    target = "abc"

    if s == target:
        return "YES"
    mismatches = [(i, s[i]) for i in range(3) if s[i] != target[i]]
    if len(mismatches) == 2:
        (i1, char1), (i2, char2) = mismatches
        if (char1 == target[i2] and char2 == target[i1]):
            return "YES"
    return "NO"


for i in range(1, t + 1):
    s = data[i]
    results.append(abc(s))

print("\n".join(results))


# for i in range(int(input())):
#     string = input()[i]

#     for j in range(0, len(string)):
#         print(string[j])
#         # if string[j] == "a" and string[j+i] == "b":
#         #     print("YES")
#         # elif string[j] == "a" and string[j+1] == "c":
#         #     print("YES")
#         # elif string[j] == "b" and string[j+1] == "a":
#         #     print("YES")
#         # else:
#         #     print("NO")
