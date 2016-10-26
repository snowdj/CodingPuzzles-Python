# Problem

http://www.lintcode.com/en/problem/sort-colors/

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers ```0```, ```1```, and ```2``` to represent the color red, white, and blue respectively.

*Notice*

- You are not suppose to use the library's sort function for this problem. 
- You should do it in-place (sort numbers in the original array).

**Example**

Given ```[1, 0, 1, 2]```, sort it in-place to ```[0, 1, 1, 2]```.

# Thoughts

- Use two pointers from the start and the end of the original array
- Comparing the two elements and swapping them if needed, to make sure the 0's are all in the left, and the 2's are all in the right

# My Solution

```
def sortColors(nums):
    if nums is None or len(nums) == 0:
        return
    
    p0 = 0
    p2 = len(nums) - 1
    i = 0
    
    while i <= p2:
        if nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        elif nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
            i += 1
        else:
            i += 1
```
