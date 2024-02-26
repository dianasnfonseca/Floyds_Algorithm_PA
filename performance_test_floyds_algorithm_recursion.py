import timeit
from floyds_algorithm_recursion import floyd
from floyds_algorithm_geeksforgeeks import floydWarshall

# Test data
# matrix = [
#     [0, 5, float('inf'), 10],
#     [float('inf'), 0, 3, float('inf')],
#     [float('inf'), float('inf'), 0, 1],
#     [float('inf'), float('inf'), float('inf'), 0]
# ]

matrix = [
    [0, 5, 4, 10],
    [1, 0, 3, 1],
    [3, 4, 0, 1],
    [5, 6, 7, 0]
]

# Performance test for your floyd function
def test_floyd():
    floyd(matrix)

# Performance test for the other floydWarshall function
def test_floydWarshall():
    floydWarshall(matrix)

# Measure performance using timeit
# num_iterations = 10000
# time_floyd = timeit.timeit(test_floyd, number=num_iterations)
# time_floydWarshall = timeit.timeit(test_floydWarshall, number=num_iterations)

# if __name__ == '__main__':
#     # Print the results
#     print("Performance comparison:")
#     print("Your floyd function:", time_floyd)
#     print("Other floydWarshall function:", time_floydWarshall)