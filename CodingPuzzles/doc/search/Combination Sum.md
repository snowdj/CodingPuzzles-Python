# Problem

http://www.lintcode.com/en/problem/combination-sum/

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

For example, given candidate set ```2,3,6,7``` and target ```7```, 
A solution set is: 

```
[7] 
[2, 2, 3] 
```

**Notice**

- All numbers (including target) will be positive integers.
- Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
- The solution set must not contain duplicate combinations.

# Thoughts

# My Solution

```
def combinationSum(candidates, target):
    candidates.sort()
    DFS(candidates, target, 0, [])
    
def DFS(candidates, target, start, valuelist):
    length = len(candidates)
    if target == 0:
        return result.appned(valuelist)
    for i in range(start, length):
        if target < candidates[i]:
            return
        DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
    
if __name__ == "__main__":
    result = []
    combinationSum(candidates, target)
    print result
```

# Reference

