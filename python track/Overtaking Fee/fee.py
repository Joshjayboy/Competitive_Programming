def cars_to_be_fined(n, enter_order, exit_order):
    fine_count = 0
    max_exit_index = -1
    for i in range(n):
        if exit_order[i] > max_exit_index:
            max_exit_index = exit_order[i]
        else:
            fine_count += 1
    return fine_count

# Read input
n = int(input())
enter_order = list(map(int, input().split()))
exit_order = list(map(int, input().split()))

# Output the result
print(cars_to_be_fined(n, enter_order, exit_order))
