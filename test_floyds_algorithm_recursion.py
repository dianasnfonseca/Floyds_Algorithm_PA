# Importing the necessary modules and classes
import unittest
from floyds_algorithm_recursion import floyd

class TestFloydAlgorithm(unittest.TestCase):
    """
    A test case class to test the Floyd's algorithm implementation.
    """

    def test_floyd(self):
        """
        Test the floyd function with different input scenarios.
        """

        # Test case 1: Simple graph
        matrix1 = [
            [0, 3, float('inf')],
            [float('inf'), 0, 2],
            [1, float('inf'), 0]
        ]
        expected_result1 = [
            [0, 3, 5],
            [float('inf'), 0, 2],
            [1, 4, 0]
        ]
        self.assertEqual(floyd(matrix1), expected_result1)

        # Test case 2: Graph with negative weights
        matrix2 = [
            [0, -1, 2],
            [float('inf'), 0, float('inf')],
            [float('inf'), 4, 0]
        ]
        expected_result2 = [
            [0, -1, 1],
            [float('inf'), 0, float('inf')],
            [3, 2, 0]
        ]
        self.assertEqual(floyd(matrix2), expected_result2)

        # Test case 3: Graph with no edges
        matrix3 = [
            [0, float('inf'), float('inf')],
            [float('inf'), 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]
        expected_result3 = [
            [0, float('inf'), float('inf')],
            [float('inf'), 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]
        self.assertEqual(floyd(matrix3), expected_result3)


# if __name__ == '__main__':
#     # Running the tests if the script is executed directly
#     unittest.main()