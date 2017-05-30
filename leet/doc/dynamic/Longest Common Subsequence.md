# Problem

http://www.lintcode.com/en/problem/longest-common-subsequence/

Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

What's the definition of Longest Common Subsequence?

- https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
- http://baike.baidu.com/view/2020307.htm

**Example**

For ```"ABCD"``` and ```"EDCA"```, the LCS is ```"A"``` (or ```"D"```, ```"C"```), return ```1```.

For ```"ABCD"``` and ```"EACB"```, the LCS is ```"AC"```, return ```2```.

# Thoughts

- Longest Common Substring vs. Longest Common Subsequence: subsequence does not have to be continuous, substring must be continuous.

- DP: D[i][j] - The longest common subsequence of s1[0:i] and s2[0:j]
- If s[i] == s[j]: D[i][j] = D[i-1][j-1] + 1
- If s[i] != s[j]: D[i][j] = max(D[i][j-1], D[i-1][j])

# My Solution

## Solution 1

```
def longestCommonSubsequence(A, B):
    n, m = len(A), len(B)
    f = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(n):
        for j in range(m):
            f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
            if A[i] == B[j]:
                f[i+1][j+1] = f[i][j] + 1

    return f[n][m]
```

## Solution 2

```
    def longestCommonSubsequence(A, B):
        # write your code here

        if A is None or B is None:
            return 0

        n, m = len(A), len(B)
        if n == 0 or m == 0:
            return 0

        f = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])

        return f[n][m]
```

# Reference

- http://www.cnblogs.com/yuzhangcmu/p/4199531.html
