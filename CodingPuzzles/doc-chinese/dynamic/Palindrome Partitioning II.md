# Problem

http://www.lintcode.com/en/problem/palindrome-partitioning-ii/

Given a string *s*, cut *s* into some substrings such that every substring is a palindrome.

Return the *minimum* cuts needed for a palindrome partitioning of *s*. 

**Example**

Given s = ```"aab"```. 

Return ```1``` since the palindrome partitioning ["aa", "b"] could be produced using 1 cut. 

# Thoughts

- 题目要求minimum number of cuts needed, 求次数，考虑用DP
- 两种DP记录表示的方法
- DP记录1: minPNum[i]: 在s[:i]的子串中，切割后全部为回文串的最小切割次数。初始状态设为最差的情况，即i-1次（切割每一个字符）
    - 怎样得到minPNum[i]的值（即状态方程是什么）？
        - 如果s[:i]是一个回文串，则minPNum[i] = 0 （不需要切割）
        - 如果s[:i]不是一个回文串，检索s[j:i] (0 <= j < i)，如果s[j:i]是一个回文串，则minPNum[i] = min(minPNum[i], minPNum[j-1]+1)
    - 最终结果：minPNum[len(s)]
- DP记录2: minPNum[i]: 在s[i:]的子串中，最少的切割可以得到多少个回文串，即minCutNum + 1。初始状态设为最差情况，即len(s)-i（切割每一个字符)
    - 怎样得到minPNum[i]的值？
        - 如果s[i:]是一个回文串，minPNum[i] = 0
        - 如果s[i:]不是一个回文串，检索s[i:j] ( i <= j < len(s)), 如果s[i:j]是一个回文串，则minPNum[i] = min(minPNum[j+1] + 1, minPNum[i])
    - 最终结果：minPNum[0] - 1
- 用一个DP记录 isPal[j][i]，记录s[j:i]是否是回文串

# My Solution

## Method 1

```
def minCut(s):
    n = len(s)

    isP = [[False for i in range(n)] for j in range(n)]
    minPNum = [0 for i in range(n)]
    # Worst case is cutting by each char
    for i in range(n):
        c = i
        for j in range(i+1):
            if s[j] == s[i] and (j+1 > i-1 or isP[j+1][i-1]):
                isP[j][i] = True
                if j == 0:
                    c = 0
                else:
                    c = min(c, minPNum[j-1] + 1)
        minPNum[i] = c

    return minPNum[-1]
```

## Method 2

```
def minCut(s):
    dp = [0 for i in range(len(s)+1)]
    p = [[False for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)+1):
        dp[i] = len(s) - i
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                p[i][j] = True
                dp[i] = min(1+dp[j+1], dp[i])
    return dp[0]-1
```

# Reference

- https://shenjie1993.gitbooks.io/leetcode-python/content/132%20Palindrome%20Partitioning%20II.html

