# Problem

http://www.lintcode.com/en/problem/minimum-subarray/

Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

*Notice*
The subarray should contain one integer at least.

**Example**
For ```[1, -1, -2, 1]```, return ```-3```. 

# Thoughts

- Solution 1: Sliding Window
  - The minsum comes from the max range of a descending range
  - What causes a descending range to end? Positive numbers and positive sums
  - Keep a tsum. If tsum > 0, reset the start point of tsum range

- Solution 2: Prefix Sum: Min Sum = Current sum - Pre Max Sum

# My Solution

## Solution 1

```
def minSubArray(nums):

    if nums is None or len(nums) == 0:
        return None
        
        minSum = sys.maxint
        tsum = 0
        for i in nums:
            tsum += i
            minSum = min(minSum, tsum)
            tsum = min(tsum, 0)
        
        return minSum
```

## Solution 2

```
def minSubArray(nums):
    if nums is None or len(nums) == 0:
        return 0
    
    minSum = nums[0]
    maxSum = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - maxSum < minSum:
            minSum = sum - maxSum
        if sum > maxSum:
            maxSum = sum
    
    return minSum
```
