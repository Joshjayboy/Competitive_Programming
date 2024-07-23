import heapq

def max_potions(n, potions):
    current_health = 0
    min_heap = []
    count = 0
    
    for potion in potions:
        if current_health + potion >= 0:
            current_health += potion
            heapq.heappush(min_heap, potion)
            count += 1
        elif min_heap and potion > min_heap[0]:
            current_health += potion - heapq.heappop(min_heap)
            heapq.heappush(min_heap, potion)
    
    return count

n = int(input().strip())
potions = list(map(int, input().strip().split()))

result = max_potions(n, potions)
print(result)
