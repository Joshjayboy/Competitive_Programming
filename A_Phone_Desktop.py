import math
def min_screens_needed(x, y):
    screens_for_2x2 = (y + 1) // 2 
    remaining_1x1_icons = x    
    if y % 2 == 1:
        remaining_1x1_icons -= 7    
    screens_for_1x1 = math.ceil(remaining_1x1_icons / 15)
    total_screens = screens_for_2x2 + max(0, screens_for_1x1)
    
    return total_screens
t = int(input())
results = []
for _ in range(t):
    x, y = map(int, input().split())
    results.append(min_screens_needed(x, y))
for result in results:
    print(result)
