# Problem

http://www.lintcode.com/en/problem/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

**Example**

Given s = "aab", return:

```
[
  ["aa","b"],
  ["a","a","b"]
]
```

# Thoughts

- DFS

# My Solution

```
def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def dfs(s, stringlist):
    if len(s) == 0:
        res.append(stringlist)
    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            dfs(s[i:], stringlist + [s[:i]])

def partition(s):
    return dfs(s, [])

if __name__ == '__main__':
    res = []
    partition("aab")
    print(res)

    del res[:]
    partition("abbac")
    print(res)
 
```

# Reference

- http://www.itdadao.com/articles/c15a171556p0.html