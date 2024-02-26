import timeit
from floyds_algorithm_recursion import floyd

def test_performance():
    # Write performance test code
    pass

if __name__ == '__main__':
    print("Performance Test Results:")
    print(timeit.timeit("test_performance()", setup="from __main__ import test_performance", number=100))
