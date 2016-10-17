# Problem

http://www.lintcode.com/en/problem/permutations/

Given a list of numbers, return all possible permutations.

**Example**

For nums = ```[1,2,3]```, the permutations are:

```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# Thoughts

Solution 1. We can get all permutations by the following steps:

```
[1]
[2,1]
[1,2]
[3,2,1]
[2,3,1]
[2,1,3]
[3,1,2]
[1,3,2]
[1,2,3]
```

Loop through the array, in each iteraction, a new number is added to different locations of results of previous iteration. Start from an empty List.

Solution 2. Recursively solve the problem. Swap each element with each element after it.

Solution 3. DFS.

# My Solution

```
def permute(nums):
    if nums is None:
        return [[]]
    elif len(nums) <= 1:
        return [nums]

    result = []
    for i, item in enumerate(nums):
        for p in permute(nums[:i] + nums[i + 1:]):
            result.append(p + [item])

    return result
```

# Reference