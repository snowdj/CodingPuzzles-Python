# Problem

http://www.lintcode.com/en/problem/two-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.

The function ```twoSum``` should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

*Notice*

You may assume that each input would have exactly one solution.

**Example**

numbers=```[2, 7, 11, 15]```, target=```9```

return ```[1, 2]```

# Thoughts

## A straight-forward solution
- For each element nums[i], check if ```target - nums[i]``` exists in nums
- Note need exclude nums[i] in the search range, eg. ```[2, 2, 3]``` and target = ```4```, the expected result is ```[1, 2]```
- Note the required return value is the index, ie. 1, 2, 3, ... n where n is the length of numbers
- Cons: Need deep copy the original list

## DP solution
- When looping through each element, keep the element index in a record: record[nums[i]] = i
- If target - nums[i] can be found in record, the return result is [hash[target - nums[i]], i]
- Why in this solution, we don't need worry about finding the element itself? Because the element is not yet added into the record when we do the search.
- Cons: Need extra space for keeping the record

# My Solution

## Solution 1

```
def twoSum(nums, target):
    if nums is None or len(nums) < 2:
        return []

    for i in range(len(nums)):
        t_nums = nums[:]
        t_nums.pop(i)
        if (target - nums[i]) in t_nums:
            return [i+1, t_nums.index(target - nums[i])+2]

    return []
```

## Solution 2

```
    def twoSum(nums, target):
        #hash用于建立数值到下标的映射
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]] + 1, i + 1]
            hash[nums[i]] = i
        #无解的情况
        return [-1, -1]
```