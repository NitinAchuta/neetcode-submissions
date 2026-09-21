class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #While the profit is getting larger, keep increasing right
        #If the profit gets smaller at any point, decrease left and increase right
        #Keep storing max profit
        l = 0
        r = 1
        maxProfit = 0

        while(r < len(prices)):
            money = prices[r] - prices[l]
            if money < 0:
                l = r
            else:
                if money > maxProfit:
                    maxProfit = money
                r += 1
        
        return maxProfit


        