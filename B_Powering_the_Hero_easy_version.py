import heapq

t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    cards = list(map(int, input().strip().split()))
    test_cases.append((n, cards))

results = []
    
for case in test_cases:
    n, cards = case
    max_heap = []
    total_power = 0
    
    for card in cards:
        if card == 0:
            if max_heap:
                total_power += -heapq.heappop(max_heap)
        else:
            heapq.heappush(max_heap, -card)
    
    results.append(total_power)

for result in results:
    print(result)
