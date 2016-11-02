# Problem

http://www.lintcode.com/en/problem/longest-common-substring/

Given two strings, find the longest common substring.

Return the length of it.

**Example**

Given A = ```"ABCD"```, B = ```"CBCE"```, return ```2```.

# Thoughts

- Use two pointers to loop through string A and B

# My Solution

```
def longestCommonSubstring(A, B):
    if A is None or B is None:
        return None

    ans = 0
    for i in range(len(A)):
        for j in range(len(B)):
            l = 0
            while i + l < len(A) and j + l < len(B) \
                and A[i+l] == B[j+l]:
                l += 1
            if l > ans:
                ans = l

    return ans
```