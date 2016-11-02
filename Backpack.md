# Problem

http://www.lintcode.com/en/problem/backpack/

Given *n* items with size Ai, an integer *m* denotes the size of a backpack. How full you can fill this backpack?

*Example*

If we have 4 items with size ```[2, 3, 5, 7]```, the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select ```[2, 3, 7]``` so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

# Thoughts

- Use DP to solve
- DP status: result[i][S] - Can you get size S from the first i elements in A?
- DP function: f[i][S] = f[i-1][S-A[i]] or f[i-1][S]
- DP initialization:
  - f[1...n][0] = True
  - f[0][1...m] = False
- DP result: max S where f[n][S] == True (1<=S<=m)

# My Solution

