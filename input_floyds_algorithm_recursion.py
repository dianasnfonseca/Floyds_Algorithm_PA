def get_input():
    """
    This function prompts the user to input the number of vertices in a graph
    and the adjacency matrix representing the graph's edges and their weights.
    
    Returns:
    - n: Number of vertices in the graph
    - matrix: Adjacency matrix representing the graph
    """
    print("Floyd's algorithm - recursion")
    print("\nPlease provide an input as the following, e.g.:")
    print("  Enter the number of vertices in the graph: 3")
    print("  Enter the adjacency matrix, row by row:")
    print("  0 1 3")
    print("  inf 0 2")
    print("  inf inf 0")
    print("\n   We can interpret this distance matrix as the following: ")
    print("       - Distance between node 0 and node 0 (or any node to itself) is 0")
    print("       - inf indicates there is no path between nodes")
    print("       - 0 1 3: means distance 1 between node 0 and 1, distance 3 between node 0 and 2")

    n = int(input("\nEnter the number of vertices in the graph: "))
    print("Enter the adjacency matrix row by row.")

    matrix = []
    for _ in range(n):
        row = input().split()
        row = [float('inf') if x == 'inf' else int(x) for x in row]
        matrix.append(row)
    return n, matrix