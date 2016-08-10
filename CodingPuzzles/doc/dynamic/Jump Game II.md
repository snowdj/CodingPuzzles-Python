# Problem

http://www.lintcode.com/en/problem/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

**Example**

Given array ```A = [2,3,1,1,4]```

The minimum number of jumps to reach the last index is ```2```. (Jump ```1``` step from index 0 to 1, then ```3``` steps to the last index.)

# Thoughts

# My Solution

## Greedy

```
def jump(A):
    if A is None:
        return 0

    index = 0
    count = 0
    last = 0
    reach = 0

    while reach >= index and index < len(A):
        if last < index:
            count += 1
            last = reach
        reach = max(reach, A[index] + index)
        index += 1

    if reach < len(A) - 1:
        return 0
    else:
        return count
```

## Dynamic Programming

```
def jump(A):
    p = [0]
    for i in range(len(A)-1):
        while (i + A[i] >= len(p) and len(p) < len(A)):
            p.append(p[i] + 1)
    return p[-1]
```