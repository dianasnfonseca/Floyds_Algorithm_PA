# Importing necessary modules and functions
import unittest  # Importing the unittest module
from input_floyds_algorithm_recursion import get_input  # Importing function to get user input
from floyds_algorithm_recursion import floyd  # Importing Floyd's algorithm function
import test_floyds_algorithm_recursion # Importing test module
import performance_test_floyds_algorithm_recursion 
import timeit

# Define num_iterations for performance tests
num_iterations = 10000

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
    Main function to execute Floyd's algorithm and optionally run tests.
    """
    # Getting input from the user
    n, matrix = get_input()
    
    # Executing Floyd's algorithm to find shortest paths
    result_matrix = floyd(matrix)
    
    # Printing the result
    print("Shortest paths between every pair of vertices:")
    print_matrix(result_matrix)

    # Asking user if they want to run tests
    run_tests = input("Do you want to run tests? (y/n): ").lower()
    
    if run_tests == 'y':
        # Running the tests

        # Explanation of tests
        print("\nWe will procede with the following tests:")
        print("1. Unit Tests: These tests ensure that each function in Floyd's algorithm works correctly.")
        print("2. Performance Tests: These tests measure the execution time of the algorithm.")
        print("   - `test_floyd`: Measures the time taken by the Floyd's algorithm.")
        print("   - `test_floydWarshall`: Measures the time taken by Floyd-Warshall algorithm.")

        print("\n1. Initializing Floyd's algorithm tests...")
        
        # Loading and running tests from test_floyds_algorithm_recursion module
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
        print("\n2. Running performance tests...")
        time_floyd = timeit.timeit(performance_test_floyds_algorithm_recursion.test_floyd, number=num_iterations)
        time_floydWarshall = timeit.timeit(performance_test_floyds_algorithm_recursion.test_floydWarshall, number=num_iterations)

        print("Time taken by floyd function:", time_floyd)
        print("Time taken by floydWarshall function:", time_floydWarshall)


# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()