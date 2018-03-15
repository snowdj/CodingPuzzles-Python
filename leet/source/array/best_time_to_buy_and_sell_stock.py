def maxProfit(prices):
    # Wrong solution, doesn't work when the last price is the lowest
    # write your code here
    if len(prices) <= 1:
        return 0

    low = prices[0]
    high = prices[0]
    for i in range(len(prices)):
        low = min(prices[i], low)
        if low == prices[i]:
            high = low
        else:
            high = max(prices[i], high)

    return high - low


def maxProfit2(prices):
    if len(prices) <= 1:
        return 0

    low = prices[0]
    maxprofit = 0
    for i in range(len(prices)):
        low = min(prices[i], low)
        maxprofit = max(maxprofit, prices[i] - low)

    return maxprofit

def test_main():
    test_prices = [2,1,2,0,3]
    print(maxProfit2(test_prices))
    print(maxProfit(test_prices))

    test_prices = [5, 1, 2, 1, 0]
    print(maxProfit2(test_prices))
    print(maxProfit(test_prices))

if __name__ == "__main__":
    test_main()