
n = int(input())

bills = 0

while n > 0:
    if n >= 100:
        bills += n // 100
        n %= 100
    elif n >= 20:
        bills += n // 20
        n %= 20
    elif n >= 10:
        bills += n // 10
        n %= 10
    elif n >= 5:
        bills += n // 5
        n %= 5
    else:
        bills += n
        n = 0

print(bills)

