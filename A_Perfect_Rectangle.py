test_cases = input()
nContainers = input()
nMarbles = input()
list_of_marbles = nMarbles.split()
sum_n = sum(map(int, list_of_marbles))
sqare_root = sum_n**0.5
if sqare_root == int(sqare_root):
    print("YES")
else:
    print("NO")
