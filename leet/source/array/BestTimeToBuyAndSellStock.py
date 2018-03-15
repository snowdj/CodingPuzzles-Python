def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit


if __name__ == "__main__":
    prices = [2,4,1,3,6]
    res = maxProfit(prices)
    print(res)