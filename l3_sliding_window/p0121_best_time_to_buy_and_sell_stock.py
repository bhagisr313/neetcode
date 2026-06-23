class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        if len(prices) == 1:
            return 0
        while(r < len(prices)):
            if prices[r] < prices[l]:
                l=r
            else:
                max_profit = max(prices[r] - prices[l],max_profit)
            r+=1
        return max_profit