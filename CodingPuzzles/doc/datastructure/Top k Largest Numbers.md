# Problem

http://www.lintcode.com/en/problem/top-k-largest-numbers/

Given an integer array, find the top k largest numbers in it.

**Example**

Given ```[3,10,1000,-99,4,100]``` and k = 3.
Return ```[1000, 100, 10]```.

# Thoughts

- The straight forward solution is sorting the array and gets the top k largest numbers
- A better solution is using heapq datastructure in Python

# My Solution

## Solution 1

```
def topk(nums, k):
    nums.sort()
    nums.reverse()
    return nums[0:k]
```

```
def topk(nums, k):
    nums.sort()
    return list(reversed(nums[-k:])) # Note function reversed does not return a list
```

## Solution 2

```
def topk(nums, k):
    heapq.heapify(nums)
    topk = heapq.nlargest(k, nums)
    return topk
```

# Reference

- About heapq: heap[0] is the smallest element. heapq.headpop(list) gets the smallest element.
- Functions of heapq: nsmallest, nlargest, headpop, push


