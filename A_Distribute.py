
n = int(input())
a = list(map(int, input().split()))

indexed_cards = [(a[i], i + 1) for i in range(n)]

indexed_cards.sort()

for i in range(n // 2):
    print(indexed_cards[i][1], indexed_cards[n - i - 1][1])
