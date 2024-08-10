testCases = int(input())

for i in range(testCases):
    val = list(map(int, input().split()))
    mini = min(val)    
    maxi = max(val)
    print(mini, maxi)
