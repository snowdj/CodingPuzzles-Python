# Problem

http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ```i```th element is the price of a given stock on day ```i```.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

**Example**

Given an example ```[2,1,2,0,1]```, return 2

# Thoughts

- The condition that you must sell the stock before you buy again makes this problem easier to be solved (no overlapping windows)
- When the price reaches a highest point in an ascending order, sell the stocks to get the maximum profit. Accumulate the profits in the process of reaching the highest price, such as ```1, 2, 3```, the accumulated profit is ```1, 2```. 
- As the problem only asks for the maximum profit, no need record each buying price and selling price

# My Solution

```
def maxProfit(prices):
    maxprofit = 0
    for i in range(1, len(prices)):
        if prices[i] >= prices[i-1]:
            maxprofit += prices[i] - prices[i-1]
    return maxprofit
```