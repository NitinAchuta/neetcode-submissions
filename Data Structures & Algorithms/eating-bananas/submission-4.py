class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Helper function to see if the curr rate works
        def checkCurrRate(rate: int, h=h,piles=piles) -> bool:
            totalTime = 0

            for i in piles:
                totalTime += math.ceil(float(i)/rate)
            return totalTime <= h
        
        low = 1
        high = max(piles)
        validPrev = 0

        while low <= high:
            rate = low + (high - low) // 2

            if checkCurrRate(rate):
                validPrev = rate
                high = rate - 1
            else:
                low = rate + 1
            
        return validPrev
        