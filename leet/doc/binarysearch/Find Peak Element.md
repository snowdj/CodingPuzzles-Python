# Find Peak Element

## Problem

http://www.lintcode.com/en/problem/find-peak-element/

There is an integer array which has the following features:
- The numbers in adjacent positions are different.
- A[0] < A[1] && A[A.length -2] > A[A.length - 1]

We define a position P is a peek if:
```
A[P] > A[P-1] && A[P] > A[P+1]
```

Find a peak element in this array. Return the index of the peak.

**Example**

Given ```[1, 2, 1, 3, 4, 5, 7, 6]```

Return index ```1``` (number 2) or ```6``` (number 7)

## Thoughts

- Binary Search
- When randomly picking a position ```t``` from the given array, there will be four possible conditions:
  - A[t-1] > A[t] > A[t+1]: Peak is on the left
  - A[t-1] < A[t] > A[t+1]: Peak is t
  - A[t-1] < A[t] < A[t+1]: Peak is on the right
  - A[t-1] > A[t], A[t+1] > A[t]: Peak is on the right, or left
  
## My Solution

```python
def findPeak(A):
    start, end = 1, len(A) - 2:
    while start + 1 < end:
        mid = start + (end - start)/2
        if A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
            start = mid
        elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
            end = mid
        elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
            return mid
        else:
            start = mid # or end = mid

    if A[start] < A[end]:
        return end

    return start

```

## Reference
