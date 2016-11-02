# Problem

http://www.lintcode.com/en/problem/first-bad-version/

The code base version is an integer start from 1 to n. One day, someone commited a bad version in the code base, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call ```isBadVersion``` to help you determine which version is the first bad one.

# Thoughts

- Binary Search
- Pay attention to the special conditions: n = 0, n = 1
- As the question asks for the first bad version, checks the start version first after the while loop 

# My Solution

```
def findFirstBadVersion(self, n):
    if n < 1:
        return None
    if n == 1:
        return 1
    
    start, end = 1, n
    while start + 1 < end:
        mid = start + (end - start)/2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid
    
    if isBadVersion(start):
        return start
    
    return end
```

# Reference

