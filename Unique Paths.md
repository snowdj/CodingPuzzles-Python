# Problem

http://www.lintcode.com/en/problem/unique-paths/

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below). 

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). 

How many possible unique paths are there?

*Notice*: *m* and *n* will be at most 100.

# Thoughts

- Initialization: row 0 column 0, value = 1 ( 1 unique path to the position)
- State function: record[i][j] = record[i-1][j] + record[i][j-1]
- i-1, j -> i, j: step down
- i, j-1 -> i, j: step right
- A m x n matrix: m rows, n columns

# My Solution

```
def uniquePaths(m, n):
    if m == 0 or n == 0:
        return 0
    
    record = [[0 for i in range(n)] for j in range(m)]
    
    for i in range(n):
        record[0][i] = 1
    for i in range(m):
        record[i][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            record[i][j] = record[i-1][j] + record[i][j-1]
    
    return record[m-1][n-1]

```