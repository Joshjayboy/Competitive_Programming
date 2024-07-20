lenght = int(input())

sequence = list(map(int, input().split()))
# sequence = [list(map(int, input().split()) for i in range(lenght))]


sequence.sort(reverse = True)
total = []
for i in range(0, len(sequence)):
    if sequence[i] >= 0:
        total.append(sequence[i])
    elif sequence[i] > 0 and sequence[i+1] < 0:
        total.append(sequence[i])
        total.append(sequence[i+1])
        print(total)
print(sum(total))



# print(lenght, sequence)