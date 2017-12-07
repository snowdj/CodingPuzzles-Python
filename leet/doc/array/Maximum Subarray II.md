# Maximum Subarray II

## Problem

http://www.lintcode.com/en/problem/maximum-subarray-ii/

Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

*Notice*

The subarray should contain at least one number

**Example**

For given ```[1, 3, -1, 2, -1, 2]```, the two subarrays are ```[1, 3]``` and ```[2, -1, 2]``` or ```[1, 3, -1, 2]``` and ```[2]```, they both have the largest sum ```7```.

## Thoughts

- DP
- Two pass
- Again this problem is similar to "Best Time to Buy and Sell Stocks III". Solution is almost the same.

## My Solution

```Python
def maxTwoSubArrays(nums):
    n = len(nums)
    a = nums[:] # Record the max sum in range [0:i]
    aa = nums[:] # Record the max sum
    for i in range(1, n):
        a[i] = max(nums[i], a[i-1] + nums[i])
        aa[i] = max(a[i], aa[i-1])
    
    b = nums[:]
    bb = nums[:]
    for i in range(n-2, -1, -1):
        b[i] = max(b[i+1] + nums[i], nums[i])
        bb[i] = max(b[i], bb[i+1])
    
    mx = - sysint - 1
    for i in range(n-1):
        mx = max(aa[i] + b[i+1], mx)
    
    return mx
```
