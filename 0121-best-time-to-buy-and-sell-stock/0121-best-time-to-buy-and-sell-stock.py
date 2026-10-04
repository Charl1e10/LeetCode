class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bday = 0
        buy = prices[0]
        sell = 0
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                day = i
                sell = 0
            if prices[i] > sell and bday < i:
                sell = prices[i]
            if sell - buy > maxprofit:
                maxprofit = sell - buy
        if maxprofit < 0:
            return 0
        else:
            return maxprofit
            
