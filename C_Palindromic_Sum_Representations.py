import sys

MOD = 10**9 + 7


def generate_palindromes(limit):
    palindromes = []

    for i in range(1, 10):
        palindromes.append(i)

    for i in range(1, 10000):
        s = str(i)
        palindromes.append(int(s + s[::-1]))
        if int(s + s[::-1]) > limit:
            break
        for j in range(10):
            palindromes.append(int(s + str(j) + s[::-1]))
            if int(s + str(j) + s[::-1]) > limit:
                break
    return [p for p in palindromes if p <= limit]

palidromes = generate_palindromes(40000)

def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for p in palidromes:
        for i in range(p, n + 1):
            dp[i] = (dp[i] + dp[i - p]) % MOD
    return dp

MAX_N = 40000
dp = count_partitions(MAX_N)

input = sys.stdin.read
data = input().split()

t = int(data[0])
output = []

for i in range(1, t + 1):
    n = int(data[i])
    output.append(str(dp[n]))

sys.stdout.write("\n".join(output) + "\n")