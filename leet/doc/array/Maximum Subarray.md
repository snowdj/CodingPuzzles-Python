# Maximum Subarray

## Problem

http://www.lintcode.com/problem/maximum-subarray/

Given an array of integers, find a contiguous subarray which has the largest sum.

**Example**

Given the array ```[−2,2,−3,4,−1,2,1,−5,3]```, the contiguous subarray ```[4,−1,2,1]``` has the largest sum = 6.

## Thoughts

- Solution 1: Sliding Window
  - The maxsum comes from the max range of a growing range
  - What causes a growing range to end? Negative numbers and negative sums
  - Keep a tsum. If tsum < 0, reset the start point of tsum range
- Solution 2: Prefix Sum: Max Sum = Current Sum - Pre Min Sum

## My Solution

### Method 1: Sliding Window

```python
def maxSubArray(nums):
    maxsum = - sys.maxint - 1 # Min Integer
    tsum = 0
    
    for i in nums:
        tsum += i
        maxsum = max(tsum, maxsum)
        tsum = max(tsum, 0)
    
    return maxsum
```

### Method 2: Prefix Sum

```python
def maxSubArray(nums):
    if nums is None or len(nums) == 0:
        return 0
    
    maxSum = nums[0]
    minSum = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - minSum > maxSum:
            maxSum = sum - minSum
        if sum < minSum:
            minSum = sum
    
    return maxSum
```

## Reference

