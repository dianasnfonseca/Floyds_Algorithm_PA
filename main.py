from input_floyds_algorithm_recursion import get_input
from floyds_algorithm_recursion import floyd

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    n, matrix = get_input()
    result_matrix = floyd(matrix)
    
    print("Shortest paths between every pair of vertices:")
    print_matrix(result_matrix)

if __name__ == "__main__":
    main()
