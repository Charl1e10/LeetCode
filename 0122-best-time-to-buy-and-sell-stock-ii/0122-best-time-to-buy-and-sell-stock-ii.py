class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = None
        sell = 0
        profit = 0
        canSell = False
        for i in range(len(prices) - 1):
            if buy is None or prices[i] < buy:
                buy = prices[i]
                canSell = True
            
            if prices[i] > buy and canSell == True and prices[i+1] <= prices[i]:
                sell = prices[i]
                profit = profit + (sell - buy)
                sell = 0
                buy = None
                canSell = False
            
        if buy is not None and prices[len(prices) - 1] > buy and canSell == True and prices[len(prices) - 1] > prices[len(prices) - 2]:
            sell = prices[len(prices) - 1]
            profit = profit + (sell - buy)

        return profit
        