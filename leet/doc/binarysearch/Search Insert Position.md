# Search Insert Position

## Problem

http://www.lintcode.com/en/problem/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

**Example**

```[1,3,5,6]```, 5 -> 2
```[1,3,5,6]```, 7 -> 4

## Thoughts

- Binary Search
- start: 0, end: len(array) - 1
- mid: start + (end - start)/2
- If target doesn't exist in the array, insert position has three posibilities
  - on the left of start (smaller than start)
  - on the right of end (larger than end)
  - between start and end

## My Solution

```python
def searchInsert(self, A, target):
    if len(A) == 0:
        return 0

    start = 0
    end = len(A) - 1
    while start + 1 < end:
        mid = start + (end - start)/2
        if target < A[mid]:
            end = mid
        elif target > A[mid]:
            start = mid
        else:
            return mid

    if A[start] == target:
        return start
    elif A[end] == target:
        return end
    elif A[start] > target:
    # target is even smaller than the first
        return start
    elif A[end] < target:
    # target is even larger than the last
        return end + 1
    else:
    # target is in the range of the given array, start is the first element that is smaller than target
        return start + 1
```

## Reference
