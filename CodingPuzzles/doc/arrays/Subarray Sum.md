# Problem

http://www.lintcode.com/en/problem/subarray-sum/

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

**Example**

Given ```[-3, 1, 2, -3, 4]```, return ```[0, 2]``` or ```[1, 3]```.

# Thoughts

## Method 1

- For nums[i], check if the sum of it and the other elements in nums[i+1:] is 0
- Complexity: O(n^2)

## Method 2

- For nums[i], calculate the sum of nums[0:i+1], and record the sum in a record hs (DP)
- DP record: hs[0] = -1, hs[sum] = i
- If sum exists in hs record, it means the sum of the range(hs[sum]+1, i) is 0
- Complexity: O(n)
- Need extra space to store the DP record

# My Solution

## Method 1

```
def subarraySum(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            return [i, i]
        
        sum = nums[i]
        
        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum == 0:
                return [i, j]
    
    return []
```

## Method 2

```
def subarraySum(nums):
    hs = {0: -1}
    sum = 0
    for i in range(len(nums)):
        sum += A[i]
        if sum in hs:
            return [hs[sum] + 1, i]
        hs[sum] = i
    return    
```

# Reference

