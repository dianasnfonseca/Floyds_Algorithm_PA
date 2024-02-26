# Floyd's Algorithm - Recursion

## Overview

This repository contains an implementation of Floyd's algorithm using recursion to find the shortest paths between all pairs of vertices in a graph. Additionally, it includes tests to ensure the correctness of the algorithm and performance tests to measure its execution time.

## Contents

- `main.py`: The main script that executes Floyd's algorithm, prompts the user for input, and optionally runs tests.
- `input_floyds_algorithm_recursion.py`: A module containing a function to prompt the user for input, including the number of vertices and the adjacency matrix representing the graph.
- `floyds_algorithm_recursion.py`: The implementation of Floyd's algorithm using recursion to find shortest paths.
- `test_floyds_algorithm_recursion.py`: Unit tests to validate the correctness of the algorithm.
- `performance_test_floyds_algorithm_recursion.py`: Performance tests to measure the execution time of the algorithm.

## Usage

To use this implementation:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Run `main.py` using Python: `python main.py`.
4. Follow the prompts to input the number of vertices and the adjacency matrix representing the graph.
5. Optionally, choose to run tests to validate the algorithm's correctness and measure its performance.

## Input Prompt

When running `main.py`, the user will be prompted to provide input in the following format:

- Enter the number of vertices in the graph.
- Enter the adjacency matrix row by row.

Example:

```
Floyd's algorithm - recursion

Please provide an input as the following, e.g.:
  Enter the number of vertices in the graph: 3
  Enter the adjacency matrix, row by row:
  0 1 3
  inf 0 2
  inf inf 0

   We can interpret this distance matrix as the following:
       - Distance between node 0 and node 0 (or any node to itself) is 0
       - inf indicates there is no path between nodes
       - 0 1 3: means distance 1 between node 0 and 1, distance 3 between node 0 and 2

Enter the number of vertices in the graph:
```

## Tests

The tests included in this repository serve the following purposes:

1. **Unit Tests**: Validate the correctness of each function in Floyd's algorithm.
2. **Performance Tests**: Measure the execution time of the algorithm.

When prompted, you can choose to run these tests to ensure the algorithm functions correctly and evaluate its performance.
