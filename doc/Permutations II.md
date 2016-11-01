# Problem

http://www.lintcode.com/en/problem/permutations-ii/

Given a list of numbers with duplicate number in it. Find all **unique** permutations.

**Example**

For numbers ```[1,2,2]```, the unique permutations are:

```
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
```

# Thoughts

# My Solution

```
def permuteUnique(num):
    length = len(num)
    if length == 0:
        return [[]]
    if length == 1:
        return [num]
    
    num.sort()
    res = []
    previousNum = None
    for i in range(length):
        if num[i] == previousNum:
            continue
        previousNum = num[i]
        for j in permuteUnique(num[:i] + num[i+1:]:
            res.append([num[i]] + j)
            
    return res
```

# Reference

