# Problem

http://www.lintcode.com/en/problem/interleaving-string

Given three strings: *s1*, *s2*, *s3*, determine whether *s3* is formed by the interleaving of *s1* and *s2*.

**Example**

For s1 = ```"aabcc"```, s2 = ```"dbbca"```

- When s3 = ```"aadbbcbcac"```, return ```true```
- When s3 = ```"aadbbcbccc"```, return ```false```

# Thoughts

- DP: dp[i][j] represents if s3[0...i+j-1] can be formed by the interleaving of s1[0...i-1] and s2[0...j-1]
- You can draw a DP matrix to illustrate the process: If the interleaving can be formed, s3[i+j-1] must be either s1[i-1] or s2[j-1]
- Each element in the DP matrix records the previous *n* elements, so the length of DP matrix records should be len(s)+1: having one extra position
- Sanity check condition: len(s3) == len(s1) + len(s2)

# My Solution

```
    def isInterleave(s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False for i in range(len(s2)+1)] for j in range(len(s1)+1) ]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
        for i in range(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s3[i-1] == s2[i-1]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1])

        return dp[len(s1)][len(s2)]
```
