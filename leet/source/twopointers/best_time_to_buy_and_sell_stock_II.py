def maxProfitMulti(prices):
    if prices is None:
        return 0
    if len(prices) <= 1:
        return 0

    maxprofit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxprofit += prices[i] - prices[i-1]

    return maxprofit

def test_main():
    test_prices = [2,1,2,3,0,3]
    print(maxProfitMulti(test_prices))
    print("Expected result: 5")

    test_prices = [1, 1, 2, 3, 4, 3]
    print(maxProfitMulti(test_prices))
    print("Expected result: 3")

if __name__ == "__main__":
    test_main()