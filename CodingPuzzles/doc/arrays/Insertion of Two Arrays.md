# Problem

http://www.lintcode.com/en/problem/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

*Notice*
- Each element in the result must be unique
- The result can be in any order

**Example**

Given nums=```[1,2,2,1]```, nums2=```[2,2]```, return ```[2]```. 

# Thoughts

- Can you use Python's built-in function or not?
- Change the arrays in-place?
- Python set vs list
    - set: guarantees the elements are unique
    - set: does not keep the order of elements
    - list operation keeps shadow of the list, but set does not. In other words, set is fast
    - set is hashable

# My Solution

## Method 1

Use set and intersection function.

```
def intersection(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    
    a = set(nums1)
    b = set(nums2)
    c = a.intersection(b)
    
    return list(c)
```

## Method 2

Use set without using the intersection function.

```
def intersection(nums1, nums2):
    # Write your code here
    if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
        return []
    
    return list(set(nums1) - (set(nums1) - set(nums2)))
```

## Method 3

Time Limit Exceeded on large data set.

```
def intersection(nums1, nums2):
    # Write your code here
    if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
        return []
    
    n2 = len(nums2)
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            nums2.append(nums1[i])

    return list(set(nums2[n2:]))
```

## Method 4

A Pythonish way. TLC on large data set.

```
def intersection(nums1, nums2):
    # Write your code here
    if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
        return []
    
    res = [item for item in nums1 if item in nums2]
    
    return list(set(res))
```

