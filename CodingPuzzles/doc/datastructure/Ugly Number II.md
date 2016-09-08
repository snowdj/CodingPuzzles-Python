# Problem

http://www.lintcode.com/en/problem/ugly-number-ii/

Ugly number is a number that only have factors ```2```, ```3``` and ```5```.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are ```1, 2, 3, 4, 5, 6, 8, 9, 10, 12...```

*Notice*

Note that ```1``` is typically treated as an ugly number.

**Example**

If ```n=9```, return ```10```. 

# Thoughts

- The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
- An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
- The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
- Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

```
(1) 1×2, 2×2, 3×2, 4×2, 5×2, … (n is an ugly number)
(2) 1×3, 2×3, 3×3, 4×3, 5×3, … (n is an ugly number)
(3) 1×5, 2×5, 3×5, 4×5, 5×5, … (n is an ugly number)
```

# My Solution

```
def nthUglyNumber(n):
    q = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    while len(q) < n:
        m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
        m = min(m2, m3, m5)
        if m == m2:
            i2 += 1
        if m == m3:
            i3 += 1
        if m == m5:
            i5 += 1 
        q.append(m)
    
    return q[-1]
```