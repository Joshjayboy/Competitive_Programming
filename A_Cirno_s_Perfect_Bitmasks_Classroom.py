# for i in range(int(input())):
#     x= int(input())
#     y = 1
#     while x & y:
#         y <<= 1
#     print(int(y))


def find_min_y(x):
    # Check if x is of the form 2^k
    if x & (x - 1) == 0:
        return x + 1
    else:
        return 1

# Reading the number of test cases
t = int(input())
results = []

for _ in range(t):
    x = int(input())
    results.append(find_min_y(x))

# Output the results for all test cases
for result in results:
    print(result)


