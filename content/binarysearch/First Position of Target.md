# Problem

http://www.lintcode.com/en/problem/first-position-of-target

For a given sorted array (ascending order) and a ```target``` number, find the first index of this number in ```O(log n)``` time complexity.

If the target number does not exist in the array, retrn ```-1```.

**Example**
If the array is ```[1,2,3,3,4,5,10]```, for given target ```3```, return ```2```.

# Thoughts

- Binary search
- The problem requires finding the 1st position, so do not stop searching if finding out the nums[mid] == target

# My Solution

```
    def binarySearch(nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums)
        while start + 1 < end:
            mid = start + (end - start)/2
            if target > nums[mid]:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
```

