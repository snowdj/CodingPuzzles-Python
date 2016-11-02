# Problem

http://www.lintcode.com/problem/merge-sorted-array/

Given two sorted integer arrays A and B, merge B into A as one sorted array.

**Example**

A = ```[1, 2, 3, empty, empty]```, B = ```[4, 5]```

After merge, A will be filled as ```[1, 2, 3, 4, 5]```

# Thoughts

- This problem is an in-place merge sort problem
- The length of the new array A after merging is len(A) + len(B), so we can do the merge sort reversely
- Another solution is using Python's sort function

# My Solution

## Method 1

```
def mergeSortedArray(A, m, B, n):
    pos = m + n - 1
    i = m - 1
    j = n - 1
    
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[pos] = A[i]
            i -= 1
        else:
            A[pos] = B[j]
            j -= 1
        
        pos -= 1
    
    while (i >= 0):
        A[pos] = A[j]
        pos -= 1
        i -= 1
    while (j >= 0):
        A[pos] = B[j]
        pos -= 1
        j -= 1
```

## Solution 2

```
def mergeSortedArray(A, m, B, n):
    for i in range(n):
        A[i+m] = B[i]
    A.sort()
```

# Reference
