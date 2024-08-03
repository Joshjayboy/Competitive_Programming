# Input reading and processing
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    c = int(data[index + 1])
    orbits = list(map(int, data[index + 2: index + 2 + n]))
    test_cases.append(((n, c), orbits))
    index += 2 + n

def minimum_destruction_cost(t, test_cases):
    results = []
    
    for case in test_cases:
        n, c = case[0]
        orbits = case[1]
        
        orbit_count = {}
        for orbit in orbits:
            if orbit in orbit_count:
                orbit_count[orbit] += 1
            else:
                orbit_count[orbit] = 1
        
        total_cost = 0
        for orbit, count in orbit_count.items():
            total_cost += min(count, c)
        
        results.append(total_cost)
    
    return results

results = minimum_destruction_cost(t, test_cases)




for result in results:
    print(result)
