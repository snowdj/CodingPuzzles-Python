# Problem

http://www.lintcode.com/en/problem/decode-ways/

A message containing letters from ```A-Z``` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given an encoded message containing digits, determine the total number of ways to decode it.

**Example**

Given encoded message ```12```, it could be decoded as ```AB``` (1 2) or ```L``` (12). The number of ways decoding ```12``` is 2. 

# Thoughts

- This problem asks for "how many" decode ways. Use DP to solve it.
- dp[i] means the decode ways for the given number's *1st* to *(i-1)th* digits
  - dp[2]: decode ways for s[0] s[1]
  - dp[3]: decode ways for s[0] s[1] s[2]
- Initialize the dp record
  - 0, 1, 2, ..., len(s) - total n+1 elements
  - dp[0] = 1, dp[1] = 1
- Check s[i-2:i]
  - If s[i-2:i] is in range (10, 26): the number of decode ways is the same as dp[i-2], but not 10 or 20: dp[i] = dp[i-2] + dp[i-1]
  - If s[i-2:i] is 10 or 20: dp[i] = dp[i-2]
  - If s[i-2:i] is 0x: dp[i] = 0
  - If s[i-2:i] > 26: dp[i] = dp[i-1]

# My Solution

```
    def numDecodings(s):
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3783897.html
