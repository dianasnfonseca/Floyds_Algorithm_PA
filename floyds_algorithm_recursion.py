def floyd(matrix):
    """
    Floyd's Algorithm: Computes the shortest paths between all pairs of vertices
    in a weighted graph using recursion.

    Args:
        matrix (list of lists): The adjacency matrix representing the weighted graph.

    Returns:
        list of lists: The shortest path distances between all pairs of vertices.
    """

    n = len(matrix)  # Number of vertices in the graph

    # Base case: If there are no vertices, return an empty list
    if n == 0:
        return []

    # Base case: If there's only one vertex, return the graph itself
    if n == 1:
        return matrix

    # Recursive case: Compute shortest paths using Floyd's algorithm
    for k in range(n):  # Intermediate vertex
        for i in range(n):  # Source vertex
            for j in range(n):  # Destination vertex
                # If vertex k is on the shortest path from i to j, update the distance
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix
