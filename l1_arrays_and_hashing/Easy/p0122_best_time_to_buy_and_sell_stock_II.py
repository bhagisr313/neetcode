class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for price in range(0,len(prices)-1):
            if prices[price+1] > prices[price]:
                total_profit += prices[price+1] - prices[price]
        return total_profit