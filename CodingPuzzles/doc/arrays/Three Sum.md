# Problem

http://www.lintcode.com/en/problem/3sum/

Given an array S of n integers, are there elements a, b, c in S such that ```a + b + c = 0```? Find all unique triplets in the array which gives the sum of zero.

*Notice*

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

**Example**

For example, given array S = ```{-1 0 1 2 -1 -4}```, A solution set is:

```
(-1, 0, 1)
(-1, -1, 2)
```

# Thoughts

- Use two pointers
- Sort the array first to make it possible to decide how to move the pointers according to the result
- Need handle the case when two numbers are equal
- Time complexity: O(n^2)

# My Solution

```
def threeSum(num):
    num.sort()
    res = []
    for i in range(len(num)-2):
        if i == 0 or num[i] > num[i-1]:
            left = i + 1
            right = len(num) - 1
            while left < right:
                if num[left] + num[right] == -num[i]:
                    res.append([num[i], num[left], num[right])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left-1]:
                        left += 1
                    while left < right and num[right] == num[right+1]:
                        right -= 1
                elif num[left] + num[right] < -num[i]:
                    while left < right:
                        left += 1
                        if num[left] > num[left-1]:
                        # Handling the case when num[left] == num[left-1]
                            break
                else:
                    while left < right:
                        right -= 1
                        if num[right] < num[right+1]:
                            break
        
    return res

```

