no_columns = int(input())
no_cubes_in_each_rows = list(map(int, input().split()))

# print(no_cubes_in_each_rows)

output = sorted(no_cubes_in_each_rows)

print(*output)