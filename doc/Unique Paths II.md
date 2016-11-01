# Problem

http://www.lintcode.com/en/problem/unique-paths-ii/

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty spaces is marked as ```1``` and ```0``` respectively in the grid.

# Thoughts

- When an obstacle is on the path, it becomes an invalid path (record[i][j] = 0)

# My Solution

```
def uniquePathsWithObstacles(grid):
    if grid is None:
        return 0
    
    row = len(grid)
    col = len(grid[0])
    
    record = [[0 for i in range(col)] for j in range(row)]
    
    for i in range(row):
        if grid[i][0] == 1:
            break
        else:
            record[i][0] = 1
    
    for i in range(col):
        if grid[0][i] == 1:
            break
        else:
            record[0][i] = 1
    
    for i in range(1, row):
        for j in range(1, col):
            if grid[i][j] == 0:
                record[i][j] = record[i-1][j] + record[i][j-1]
            else:
                record[i][j] = 0
    
    return record[row-1][col-1]
    
```