# from collections import defaultdict
# test_cases = input()
# no_of_vertices, no_of_edges = [map(int, input().split()) for _ in range(test_cases)]

# # print(no_of_vertices, no_of_edges)

# no_of_vertices_connected_by_an_edge = [
#     list(map(int, input().split())) for _ in range(no_of_edges)]

# # print(no_of_vertices_connected_by_an_edge)

# dictionary = defaultdict(list)

# for i, j in no_of_vertices_connected_by_an_edge:
#     dictionary[i].append(j)
#     dictionary[j].append(i) 

# # print(dictionary)

# for keys in dictionary.values():
#     x = len(keys)
#     y = len(keys) -2
# print(x, y)
#     # continue
#     # print(keys)
# # print("here",len(keys))

# # x = len(keys)
# # y = len(keys) -2

# # print(x, y)




def solve(test_cases):
    results = []
    
    for n, m, edges in test_cases:
        from collections import defaultdict, Counter

        # Initialize graph as adjacency list
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find the central vertex (vertex with the maximum degree)
        degrees = Counter({node: len(neighbors) for node, neighbors in graph.items()})
        central_vertex = degrees.most_common(1)[0][0]
        x = degrees[central_vertex]

        # Determine y by checking the degree of any vertex connected to the central vertex
        y = degrees[graph[central_vertex][0]] - 1
        
        results.append((x, y))
    
    return results

results = solve(test_cases)
for result in results:
    print(result[0], result[1])