import sys
import math
input = sys.stdin.readline


MAX = 1000000
is_prime = [True] * (MAX - 1)
for i in range(2, MAX + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False


def main():
    n = int(input())
    a = list(map(int, input().split()))

    for num in a:
        snum = int(math.sqrt(num))
        if num == 4:
            print("YES")
        elif num % 2 == 0:
            print("NO")
