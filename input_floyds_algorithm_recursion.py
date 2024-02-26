def get_input():
    """
    This function prompts the user to input the number of vertices in a graph
    and the adjacency matrix representing the graph's edges and their weights.
    
    Returns:
    - n: Number of vertices in the graph
    - matrix: Adjacency matrix representing the graph
    """
    n = int(input("Enter the number of vertices in the graph: "))
    print("Enter the adjacency matrix row by row.")
    print("Use space-separated integers to represent edges, and 'inf' for absence of an edge.")
    print("For example, if the edge between vertices 1 and 2 has weight 3, and there is no edge between vertices 1 and 3, the input for a 3x3 matrix would be '0 3 inf' on separate lines.")

    matrix = []
    for _ in range(n):
        row = input().split()
        row = [float('inf') if x == 'inf' else int(x) for x in row]
        matrix.append(row)
    return n, matrix