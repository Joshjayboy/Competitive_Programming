def min_steps_to_divisible_by_25(n):
    str_n = str(n)
    length = len(str_n)
    pairs = ['00', '25', '50', '75']
    min_steps = float('inf')
    
    for pair in pairs:
        i = length - 1
        count = 0
        found = 0
        
        for char in reversed(str_n):
            if char == pair[1 - found]:
                found += 1
                if found == 2:
                    break
            else:
                count += 1
        
        if found == 2:
            min_steps = min(min_steps, count)
    
    return min_steps

# Example usage
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(min_steps_to_divisible_by_25(n))

for result in results:
    print(result)
