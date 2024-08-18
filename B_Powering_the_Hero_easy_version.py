import heapq

t = int(input().strip())
cases = []

for _ in range(t):
    n = int(input().strip())
    cards = list(map(int, input().split()))
    cases.append((n, cards))

results = []
    
for case in cases:
    n, cards = case
    max_heap = []
    totalPower = 0
    
    for card in cards:
        if card == 0:
            if max_heap:
                totalPower += -heapq.heappop(max_heap)
        else:
            heapq.heappush(max_heap, -card)
    
    results.append(totalPower)

for x in results:
    print(x)