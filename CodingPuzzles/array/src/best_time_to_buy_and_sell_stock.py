def maxProfit(prices):
    # write your code here
    if len(prices) <= 1:
        return 0

    low = prices[0]
    high = 0
    for i in range(len(prices)):
        if prices[i] < low:
            low = prices[i]
        if prices[i] > high:
            high = prices[i]

    return high - low

if __name__ == "__main__":
    test_prices = [2,1,2,0,]