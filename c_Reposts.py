n= int(input())

repost = [input() for _ in range(n)]

from collections import deque

queue = deque()

for i in range(0, n):    
    queue.append(repost[i])

visited= set()
count =2
while queue:
    x = queue.popleft()    

    y = x.split()

    t = y[0]
    p = t.lower()

    m = y[2]
    n = m.lower()
 
    if (p, n) not in visited and n != "polycarp":
        count += 1
        
        visited.add((p,n))
print(count)
    
