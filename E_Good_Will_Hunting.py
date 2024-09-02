a, b = map(int, input().split())
XOR = a ^ b
highest_bit = 1
while highest_bit <= XOR:
    highest_bit <<= 1
print(highest_bit - 1)
