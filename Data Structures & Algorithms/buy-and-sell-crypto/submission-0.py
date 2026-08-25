class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we know left is buying and r is selling since time only move forwards
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            
            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:

                l = r
            r += 1
    
        return maxP
