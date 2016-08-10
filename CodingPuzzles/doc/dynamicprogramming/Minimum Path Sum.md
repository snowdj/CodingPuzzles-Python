# Problem

http://www.lintcode.com/en/problem/minimum-path-sum/

Give a *m x n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

# Thoughts

- Record is a matrix to store the sum of numbers along the path, till each position
- Initialization: record[0][j], record[i][0]

# My Solution

```
def minPathSum(grid):
    if grid is None:
        return 0

    row = len(grid)
    col = len(grid[0])

    record = [[0 for i in range(col)] for j in range(row)]

    # Initialize the first row and column of record (stores the sum of numbers along the path)
    for i in range(col):
        if i == 0:
            record[0][i] = grid[0][i]
        else:
            record[0][i] = record[0][i-1] + grid[0][i]
    for j in range(row):
        if j == 0:
            record[j][0] = grid[j][0]
        else:
            record[j][0] = record[j-1][0] + grid[j][0]

    for i in range(1, row):
        for j in range(1, col):
            record[i][j] = min(record[i][j-1] + grid[i][j], record[i-1][j] + grid[i][j]

    return record[row-1][col-1]

```
