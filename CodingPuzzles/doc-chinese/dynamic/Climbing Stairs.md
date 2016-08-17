# Problem

http://www.lintcode.com/en/problem/climbing-stairs/

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example**

Given an example n=3, 1+1+1=2+1=1+2=3

return 3

# Thoughts

- One dimensional DP
- f[i]: the number of methods to climb to the position i
- Function: f[i] = f[i-1] + f[i-2] (Climb from position i-1, or position i-2)
- Intialize: f[0] = 1
- Answer: f[n]
- If the problem is not related to matrix, use a N+1 position array if there are N numbers. The 0 position is for initialization only.

# My Solution

```
def climbChairs(n):
    if n <= 1:
        return 1
    
    dp = [1 for i in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```