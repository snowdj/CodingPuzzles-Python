# Problem

http://www.lintcode.com/en/problem/subsets-ii/

Given a list of numbers that may has duplicate numbers, return all possible subsets

*Notice*

- Each element in a subset must be in non-descending order.
- The ordering between two subsets is free.
- The solution set must not contain duplicate subsets.

**Example**

If S = ```[1,2,2]```, a solution is:

```
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

# Thoughts

- Standard DFS
- Similar to Subsets I, the difference is this problem need check if a set already in result

# My Solution

```
def subsets(self, S):
    def dfs(depth, start, valuelist):
        if valuelist not in res:
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