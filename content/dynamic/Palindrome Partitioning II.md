# Problem

http://www.lintcode.com/en/problem/palindrome-partitioning-ii/

Given a string *s*, cut *s* into some substrings such that every substring is a palindrome.

Return the *minimum* cuts needed for a palindrome partitioning of *s*. 

**Example**

Given s = ```"aab"```. 

Return ```1``` since the palindrome partitioning ["aa", "b"] could be produced using 1 cut. 

# Thoughts

- The problem asks for the minimum number of cuts needed, use DP to resolve it
- isP[j][i]: Is s[j:i] a palindrome?
- minPNum[i]: The minimum number of cuts needed for getting very substring is a palindrome in s[:i+1]
- Initial states: Cutting by each character, so minPNum[i] = i
- Function:
    minPNum[i] = 0, if s[:i+1] is a palindrome
    minPNum[i] = min(minPNum[i], minPNum[j-1]+1), if s[j:i+1] is a palindrome
- Result: minPNum[-1]

# My Solution

```
    def minCut(s):
        n = len(s)

        isP = [[False for i in range(n)] for j in range(n)]
        minPNum = [0 for i in range(n)]
        # Worst case is cutting by each char
        for i in range(n):
            m = i
            for j in range(i+1):
                if s[j] == s[i] and (j+1 > i-1 or isP[j+1][i-1]):
                    isP[j][i] = True
                    if j == 0:
                        m = 0
                    else:
                        m = min(m, minPNum[j-1] + 1)
            minPNum[i] = m

        return minPNum[-1]
```

# Reference

- https://shenjie1993.gitbooks.io/leetcode-python/content/132%20Palindrome%20Partitioning%20II.html

