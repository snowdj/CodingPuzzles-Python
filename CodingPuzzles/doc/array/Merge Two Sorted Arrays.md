# Problem

http://www.lintcode.com/en/problem/merge-two-sorted-arrays/

Merge two given sorted integer array *A* and *B* into a new sorted integer array.

**Example**

A=```[1,2,3,4]```

B=```[2,4,5,6]```

return ```[1,2,2,3,4,4,5,6]```

# Thoughts

- Basic merge sort algorithm

# My Solution

```
    def mergeSortedArray(A, B):
        # write your code here
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A
        
        res = []
        while len(A) > 0 and len(B) > 0:
            if A[0] <= B[0]:
                res.append(A.pop(0))
            else:
                res.append(B.pop(0))
        
        if len(A) > 0:
            res += A
        if len(B) > 0:
            res += B
        
        return res
```