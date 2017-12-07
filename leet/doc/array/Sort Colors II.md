# Sort Colors II

## Problem

http://www.lintcode.com/en/problem/sort-colors-ii/

Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

*Notice*

You are not suppose to use the library's sort function for this problem.

**Example**

Given colors=```[3, 2, 2, 1, 4]```, ```k=4```, your code should sort colors in-place to ```[1, 2, 2, 3, 4]```.

## Thoughts

- A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory.
  - Two-pass algorithm: first pass, count the number of each color
  - Second pass, place the color according to their counts

- Another method is using the similar method as in Sort Color for three colors.  

## My Solution

```python
    def sortColors2(self, colors, k):
        # write your code here
        count = 0
        start = 0
        end = len(colors) - 1
        remain = list(colors)
        while count < k:
            if not remain:
                break
            minColor = min(remain)
            maxColor = max(remain)
            pColor1, pColor2 = self.sortColors(colors, minColor, maxColor, start, end)
            start = pColor1
            end = pColor2
            count += 2
            remain = colors[start:end+1] #start和end都应该包含在下一次里面
        return colors
    
    def sortColors(self, colors, color1, color2, start, end):
        # left和right表示的是两个颜色'下一个'的位置'
        left = start
        right = end
        index = start
        while index <= right:
            if colors[index] == color1:
                colors = self.swap(colors, left, index)
                left += 1
                index += 1
            elif colors[index] == color2:
                colors = self.swap(colors, right, index)
                right -= 1
            else:
                index += 1

        return left, right

    def swap(self, nums, i, j):
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        return nums
```

## Reference

- https://lefttree.gitbooks.io/leetcode-categories/content/quickSelect/sortColors2.html
- http://www.cnblogs.com/yuzhangcmu/p/4177326.html

