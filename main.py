# Importing necessary modules and functions
import unittest  # Importing the unittest module
from input_floyds_algorithm_recursion import get_input  # Importing function to get user input
from floyds_algorithm_recursion import floyd  # Importing Floyd's algorithm function
import test_floyds_algorithm_recursion # Importing test module
#import performance_test_floyds_algorithm_recursion 


def print_matrix(matrix):
    """
    Prints a matrix row by row.

    Args:
    matrix (list): The matrix to be printed.
    """
    for row in matrix:
        print(row)

def main():
    """
    Main function to execute Floyd's algorithm and run tests.
    """
    # Getting input from the user
    n, matrix = get_input()
    
    # Executing Floyd's algorithm to find shortest paths
    result_matrix = floyd(matrix)
    
    # Printing the result
    print("Shortest paths between every pair of vertices:")
    print_matrix(result_matrix)

    # Running the tests
    print("\nInitializing Floyd's algorithm tests...")
    
    # Loading and running tests from TestFloydAlgorithm module
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_floyds_algorithm_recursion)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Checking if any tests failed
    if result.failures:
        print("\nSome tests failed. Please review the test output.")
    else:
        print("\nAll tests passed successfully.")

    # Run performance tests
    #print("\nRunning performance tests...")
    #performance_test_floyds_algorithm_recursion.test_floyd()
    #performance_test_floyds_algorithm_recursion.test_floydWarshall()

# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()
