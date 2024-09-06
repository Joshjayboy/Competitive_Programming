from itertools import combinations

n, m = map(int, input().split())
names = []

for _ in range(n):
    name = input()
    names.append(name)


rivalries = set()
for _ in range(m):
    a, b = input().split()
    rivalries.add((a, b))
    rivalries.add((b, a))  


def is_valid_team(team):
    
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            if (team[i], team[j]) in rivalries:
                return False
    return True


largest_team = []


for i in range(1, n + 1):
    
    for subset in combinations(names, i):
        if is_valid_team(subset):
          
            if len(subset) > len(largest_team):
                largest_team = list(subset)


largest_team.sort()


print(len(largest_team))
for member in largest_team:
    print(member)