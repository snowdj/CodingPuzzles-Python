# Problem

http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the *ith* element is the price of a given stock on day *i*.

Design an algorithm to find the **maximum** profit. You may complete at most *two* transactions.

*Notice*

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

**Example**
Given an example ```[4,4,6,1,1,4,2,5]```, return ```6```.

# Thoughts

- The constraint is you must sell the stock before you buy again, and do at most two transactions
- As you need pick the best two transactions which will cause maximum profit, you'll need record a history of the possible transactions
- Use two records f1 and f2. f1[i] means the maximum profit you can get before price[i]. f2[i] means the maximum profit you can get after price[i]. So the overall maximum profit is f1[i] + f2[i].
- How to get f1? Find the minimum buying price. Check from the 1st price to the last price, maximum profit you can get before price[i] is the maximum price[i] - minimum value in range [0:i]
- How to get f2? Find the maximum selling price. Check from the last price to the 1st price, maximum profit you can get after price[i] is the maximum value - price[i] in range[i+1:]

# My Solution

```
def maxProfit(prices):
    length = len(prices)
    if length == 0:
        return 0
    
    f1 = [0 for i in range(length)]
    f2 = [0 for i in range(length)]
    
    minV = prices[0]
    for i in range(1, length):
        minV = min(minV, prices[i])
        f1[i] = max(f1[i-1], prices[i] - minV)
    
    maxV = prices[length-1]
    for i in range(length-2, -1, -1):
        maxV = max(maxV, prices[i])
        f2[i] = max(f2[i+1], maxV - prices[i])
    
    res = 0
    for i in range(length):
        if f1[i] + f2[i] > res:
            res = f1[i] + f2[i]
    
    return res
```