class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0

        l = 0
        r = l + 1

        while r < len(prices):
            currP = prices[r] - prices[l]
            maxP = max(currP, maxP)

            if currP > 0:
                r += 1
            else:
                l = r
                r += 1

        return maxP
            
        