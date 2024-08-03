
n, m = map(int, input().split())
problems = list(map(int, input().split()))
difficulty_count = [0] * (n + 1)
result = []

for problem in problems:
    difficulty_count[problem] += 1

    if all(difficulty_count[1:]):
        for i in range(1, n + 1):
            difficulty_count[i] -= 1
        result.append('1')
    else:
        result.append('0')

print(''.join(result))
