# Problem

http://www.lintcode.com/en/problem/maximum-subarray-difference/

Find two non-overlapping subarrays A and B, which ```|SUM(A) - SUM(B)|``` is the largest.

Return the largest difference.

*Notice*
The subarray should contain at least one number

**Example**
For ```[1, 2, -3, 1]```, return ```6```

# Thoughts

- Similar problem: Maximum Subarray II
- DP record: Check the maximum subarray and minimum subarray in the range [0:i] and range [i+1:]
- Check the DP record, find the max(abs(left max - right min), abs(left min - right max))

# My Solution

```
def maxDiffSubArrays(nums):
    n = len(nums)
    mx1 = [0] * n
    mx1[0] = nums[0]
    mn1 = [0] * n
    mn1[0] = nums[0]
    
    forward = [mn1[0], mx1[0]]
    array_f = [0] * n
    array_f[0] = forward[:]
    for i in range(1, n):
        mx1[i] = max(mx1[i-1] + nums[i], nums[i])
        mn1[i] = min(mn1[i-1] + nums[i], nums[i])
        forward = [min(mn1[i], forward[0]), max(mx1[i], forward[1])]
        array_f[i] = forward[:]
    
        mx2 = [0]*n
        mx2[n-1] = nums[n-1]
        mn2 = [0]*n
        mn2[n-1] = nums[n-1]
        backward = [mn2[n-1], mx2[n-1]]
        array_b = [0]*n
        array_b[n-1] = backward[:] 
        for i in range(n-2, -1, -1):
            mx2[i] = max(mx2[i+1] + nums[i], nums[i])
            mn2[i] = min(mn2[i+1] + nums[i], nums[i])
            backward = [min(mn2[i], backward[0]), max(mx2[i], backward[1])]
            array_b[i] = backward[:]
        result = -65535
        for i in range(n-1):
            result = max(result, abs(array_f[i][0] - array_b[i+1][1]), abs(array_f[i][1] - array_b[i+1][0]))
        return result
    
```

# Reference

- http://www.it610.com/article/1292209.htm

