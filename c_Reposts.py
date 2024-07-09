n= int(input())

repost = [input() for _ in range(n)]

from collections import deque

queue = deque()

for i in range(0, n):    
    queue.append(repost[i])

visited= set()
count =2
depths = {"polycarp": 1}
while queue:
    x = queue.popleft()    

    y = x.split()

    t = y[0]
    p = t.lower()

    m = y[2]
    n = m.lower()

    depths[p] = depths[n]+1
 
print(max(depths.values()))
    
