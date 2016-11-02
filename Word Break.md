# Problem

http://www.lintcode.com/en/problem/word-break/

Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

**Example**

Given s = ```"lintcode"```, dict = ```["lint", "code"]```. 

Return true because "lintcode" can be break as ```"lint code```. 

# Thoughts

# My Solution

## Method 1: Possibly exceeds Time Limit

```
def wordBreak(s, dict):
    if len(dict) == 0:
        return len(s) == 0
    
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    
    for i in range(1, n+1):
        for k in range(i):
            if dp[k] and s[k:i] in dict:
                dp[i] = True
    
    return dp[len(s)]
```

## Method 2: Optimized

```
def wordBreak(s, dict):
    if len(dict) == 0:
        return len(s) == 0
    
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    
    maxLen = max([len(w) for w in dict])
    for i in range(1, n+1):
        for j in range(1, min(i, maxLen) + 1):
            if not dp[i-j]:
                continue
            if s[i-j : i] in dict:
                dp[i] = True
                break
    
    return dp[n]
```

# Reference

- https://www.youtube.com/watch?v=WepWFGxiwRs
