# Two Sum Closet

## Problem

http://www.lintcode.com/en/problem/two-sum-closest/

Given an array ```nums``` of n integers, find two integers in nums such that the sum is closest to a given number, *target*.

Return the difference between the sum of the two integers and the target.

**Example**

Given array ```nums = [-1, 2, 1, -4]```, and target = ```4```.

The minimum difference is ```1```. (4 - (2 + 1) = 1).

## Thoughts

### A straight forward solution

- For each number nums[i] in the array, check nums[i+1:] to get the sum of two integers. 
- Record the difference between the sum and the target. Return the minimum value in the difference record.

### A better solution: using two pointers
- First, sort the list ascending (sorting can be very useful for some problems, think about it)
- Use two pointers at the front (i) and the end (j). Sum nums[i] and nums[j]. As the list is sorted, we can decide whether the closet sum can be obtained by increasing i, or decreasing j
  - If nums[i] + nums[j] > target, decrease j; record the min diff
  - If nums[i] + nums[j] < target, increase j; record the min diff
- Why we can use two pointer approach for this problem but not the Two Sum problem if there are duplicate values in the nums array?
  - Because the Two Sum problem asks for the exact element index. Duplicate values could produce wrong element indexes in the result.
  - This problem does not care about index, it asks only for the difference between target and 2sum value.

## My Solution

```python
def twoSumClosest(nums, target):
    nums.sort()
    i, j = 0, len(nums) - 1
    
    diff = sys.maxint
    
    while i < j:
        if nums[i] + nums[j] < target:
            diff = min(diff, target - nums[i] - nums[j])
            i += 1
        else:
            diff = min(diff, nums[i] + nums[j] - target)
            j -= 1
    
    return diff
```

## Reference
