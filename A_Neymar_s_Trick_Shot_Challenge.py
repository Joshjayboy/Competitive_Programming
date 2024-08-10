
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
X = int(data[1])
distances = list(map(int, data[2:]))

position = 0
count = 1

for i in range(N):
    position += distances[i]
    if position <= X:
        count += 1
    else:
        break
    
print(count)
