# Edit Distance

Note: 
- Edit Distance algorithm was used when I implemented a spell checker for configuration used in a GPU infrastructure tool (Jan 2017).

## Problem

http://www.lintcode.com/en/problem/edit-distance/

Given two words *word1* and *word2*, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
 
 You have the following 3 operations permitted on a word:
 
 - Insert a character
 - Delete a character
 - Replace a character

**Example**

Given word1 = ```"mart"``` and word2 = ```"karma"```, return ```3```. 

## Thoughts

- Hamming Distance vs. Edit Distance
  - edit distance <= hamming distance
- DP record: a matrix dp[i][j]
  - dp[i][j]: the edit distance from word0[0..i-1] to word1[0..j-1]
  - dp[0][j] = j # insert j letters
  - dp[i][0] = i # delete i letters
- The equation of getting the minimal edit distance is
  - dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
  - Check out the reference video (by Ben Langmead, or from MIT) to learn more about this equation
  - To x[i]->y[j], three possibly ways
    - Replace x[i] with y[j] if x[i] != y[j]
    - Insert y[j] before x[i] to make (possibly) x[i] = y[j+1], then continue processing x[i:] and y[j+1:]
    - Delete x[i] to makes (possibly) x[i+1] = y[j], then continue processing x[i+1:] and y[j:]
    - So the DP equation is

```
DP(i,j) = min(
 cost of replacing x[i] -> y[j] + DP(i+1, j+1),
 cost of inserting y[j] + DP(i, j+1),
 cost of deleting x[i] + DP(i+1, j)
)
```    

# My Solution

```python
def minDistance(word1, word2):
    # write your code here
    m = len(word1)+1
    n = len(word2)+1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i]=i
    for i in range(m):
        dp[i][0]=i
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
    return dp[m-1][n-1]
```

# Reference

- https://www.youtube.com/watch?v=We3YDTzNXEk

- https://www.youtube.com/watch?v=eAVGRWSryGo 

- https://www.youtube.com/watch?v=ocZMDMZwhCY
MIT CS Course. Explains edit distance DP algorithm with thinking in a recursive way. Easy to understand.
