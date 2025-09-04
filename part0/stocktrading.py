"""
Authors: Deepesh K, Dhaiwat K
Creation date: 09/03/2025
Stock Trading - calculates the maximum profit by choosing a single day
to buy one stock and choosing a different day in the future to sell that stock
"""

def maxProfit(prices):
    if not prices:
        return 0

    low = prices[0]
    maxprofit = 0

    for i in prices[1:]:
        if (i < low):
            low = i
        else:
            profit = i - low
            if profit > maxprofit:
                maxprofit = profit
            # maxprofit = max(maxprofit, i-low)

    return maxprofit


def main():
    maxProfit([])
    print("Test 1:", maxProfit([7, 1, 5, 3, 6, 4]) == 5)  # Buy at 1, sell at 6
    print("Test 2:", maxProfit([7, 6, 4, 3, 1]) == 0)  # Always falling
    print("Test 3:", maxProfit([1, 2, 3, 4, 5]) == 4)  # Buy at 1, sell at 5
    print("Test 4:", maxProfit([5]) == 0)
    print("Test 5:", maxProfit([]) == 0)
    print("Test 6:", maxProfit([3, 2, 6, 1, 4]) == 4)  # Buy at 2, sell at 6
    print("Test 7:", maxProfit([2, 4, 1, 7]) == 6)  # Buy at 1, sell at 7
    print("Test 8:", maxProfit([0, 0, 0, 0, 0]) == 0)
    print("Test 9:", maxProfit([3, 2, 6, 1, 4]) == 4)
    print("Test 9:", maxProfit([3, 10, 1, 5])==7)
    print("Test 10:", maxProfit([])==0)


if __name__ == "__main__":
    main()