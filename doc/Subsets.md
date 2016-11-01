# Problem

http://www.lintcode.com/en/problem/subsets/

Given a set of distinct integers, return all possible subsets.

*Notice*

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

**Example**

If S = ```[1,2,3]```, a solution is:

```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

# Thoughts

- DFS

# My Solution

```
def subsets(self, S):
    def dfs(depth, start, valuelist):
        res.append(valuelist)
        if depth == len(S):
            return
        for i in range(start, len(S)):
            dfs(depth+1, i+1, valuelist+[S[i]])
    
    S.sort()
    res = []
    dfs(0, 0, [])
    return res
```

# Reference

