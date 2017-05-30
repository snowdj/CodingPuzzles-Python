# Problem

http://www.lintcode.com/en/problem/longest-increasing-subsequence/

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

**Note**

What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

**Example**

For ```[5, 4, 1, 2, 3]```, the LIS is ```[1, 2, 3]```, return 3
For ```[4, 2, 4, 5, 3, 7]```, the LIS is ```[2, 4, 5, 7]```, return 4

# Thoughts

- DP[:n]: n is the length of the list L
- DP[i] means the LIS of L[i]
- To calculate DP[i], need check L[0:i]
- Result: DP[len(L)-1]
- Initial states: dp[0:i] = 1

# My Solution

## Method 1

```
    def longestIncreasingSubsequence(nums):
        if nums is None or len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
```

## Method 2

```
    def longestIncreasingSubsequence(numbs):
        if nums is None or not nums:
            return 0
        
        lis = [1] * len(nums)
        
        for idx, val in enumerate(nums):
            for prev in xrange(idx):
                if nums[prev] <= val:
                    lis[idx] = max(lis[idx], lis[prev] + 1)
        
        return max(lis)
```

