number_of_node = input()

edges = [list(map(int, input().split())) for _ in range(number_of_node - 1)]

# sequence = solve([(number_of_node, number_of_node - 1, edges)])

sequence = [list(map(int, input().split()))]
print(number_of_node)
print(edges)
print(sequence)