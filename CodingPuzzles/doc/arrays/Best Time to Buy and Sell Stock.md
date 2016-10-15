# Problem

Say you have an array for which the ```i```th element is the price of a given stock on day ```i```.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Thoughts

- Iterate each price and keep calculating the lowest price and the max profit (max(price[i] - lowest_price))
- The method that finds the lowest price and the highest price will not work. Because in the stock buy/sell case, the low price must come before high price
- The other idea is iterating each price, find the lowest price so far, and find the highest price appears after the lowest price. Possible maxprofit = highest_price - lowest_price. Final maxprofit = max(maxprofits).

# My Solution

```
def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    
    low = prices[0]
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < low:
            low = prices[i]
        maxprofit = max(maxprofit, prices[i] - low)
    
    return maxprofit
```