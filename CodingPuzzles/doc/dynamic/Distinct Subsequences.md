# Problem

http://www.lintcode.com/en/problem/distinct-subsequences/

Given a string *S* and a string *T*, count the number of distinct subsequences of *T* in *S*.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, ```"ACE"``` is a subsequence of ```"ABCDE"``` while ```"AEC"``` is not).

**Example**

Given S = ```"rabbbit"```, T = ```"rabbit"```, return ```3```. 

# Thoughts

- The problem asks how many subsequences in S are T, so the DP function represents how many subsequences in S[sub] is T[sub].
- DP[i][j]: How many subsequences in S[0:i] is T[0:j]
- if S[i] != T[j]: DP[i][j] = DP[i][j-1]
- if S[i] == T[j]: DP[i][j] = DP[i][j-1] + DP[i-1][j]

# My Solution

```
    def numDistinct(S, T):
        # write your code here

        dp = [ [0 for i in range(len(T)+1)] for j in range(len(S)+1) ]
        for j in range(len(S)+1):
            dp[j][0] = 1

        for i in range(1, len(S)+1):
            for j in range(1, min(i+1, len(T)+1)):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(S)][len(T)]
```

# Reference

- http://blog.csdn.net/abcbc/article/details/8978146

