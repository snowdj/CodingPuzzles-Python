# Problem

http://www.lintcode.com/en/problem/triangle/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

**Example**

Given the following triangle:

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is 11 (i.e., 2+3+5+1=11)

# Thoughts

- The solution of this problem depends heavily on the triangle's property
  - Each element of the lowest row in the triangle holds a minimum sum from top to this bottom element
  - The minimum sum is the minimum value of all the lowest elements
  - In each row, element 0's path sum is record[0] + triangle[row][j] (assuming allowing moving to j, j+1)
  - Last element (len(row) - 1): path sum is record[j] + triangle[row][j] (this position j does not exist in previous row)
  - Other elements: the previously element can be j-1 or j, so the path sum is the minimum of record[j-1] + triangle[row][j] and record[j] + triangle[row][j]

- Question: What if when j >= 1, the next step can move to j-1, j and j+1 ?

# My Solution

```
def minimumTotal(triangle):
    if triangle is None:
        return 0

    height = len(triangle)
    record = [0 for i in range(height)]
    record[0] = triangle[0][0]

    for i in range(1, height):
        for j in range(len(triangle[i] -1, -1, -1):
            if j == 0:
                record[j] = record[j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                record[j] = record[j-1] + triangle[i][j]
            else:
                record[j] = min(record[j-1], record[j]) + triangle[i][j]

```