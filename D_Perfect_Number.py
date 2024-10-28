k = int(input())
def digitsum(n):
    return sum(int(d) for d in str(n))

def perfect(k):
    count = 0
    number = 18
    
    while count < k:
        number += 1
        if digitsum(number) == 10:
            count += 1
            
    return number


print(perfect(k))
