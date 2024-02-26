def floyd(graph, u, v, k):
    # Base case
    if k == 0:
        return graph[u][v]
    
    # Recursive case
    return min(floyd(graph, u, v, k-1), floyd(graph, u, k, k-1) + floyd(graph, k, v, k-1))

# Example graph
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

num_vertices = len(graph)
for i in range(num_vertices):
    for j in range(num_vertices):
        for k in range(num_vertices):
            graph[i][j] = floyd(graph, i, j, k)

print("Shortest distances between every pair of vertices:")
for row in graph:
    print(row)
