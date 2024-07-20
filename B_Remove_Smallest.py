for i in range(input()):
    n = input()
    integers = list(input().strip())
    for i in range(0, len(integers)):
        if i - i+1 <= 1:
            integers.remove(min(integers[i], integers[i+1]))
