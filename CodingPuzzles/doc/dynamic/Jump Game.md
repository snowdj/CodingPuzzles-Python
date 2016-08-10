# Problem

http://www.lintcode.com/en/problem/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

*Notice*
This problem has two method which is ```Greedy``` and ```Dynamic Programming```.
The time complexity of ```Greedy``` is ```O(n)```.
The time complexity of ```Dynamic Programming``` method is ```O(n^2)```.

**Example**

A = ```[2,3,1,1,4]```, return ```true```
A = ```[3,2,1,0,4]```, return ```false```

# Thoughts

- Check on each position: if can be jumped from any of its preceeding positions

# My Solution

```
def canJump(A):
    if A is None:
        return False

    canJump = [False for i in range(len(A))]
    canJump[0] = True

    for i in range(1, len(A)):
        for j in range(0, i):
            if canJump[j] and (A[j] + j >= i):
                canJump[j] = True
                break
        if canJump[i] == False:
            return False

    return canJump[len(A)-1]
```