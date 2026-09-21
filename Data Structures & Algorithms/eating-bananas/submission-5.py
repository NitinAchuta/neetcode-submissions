class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Helper function to see if the curr rate works

        def checkCurrRate(rate, piles=piles, h=h) -> bool:

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p) / rate)
                if totalTime > h:
                    return False
            return True

        low, high = 1, max(piles)
        validPrev = 0

        while low <= high:
            
            currRate = (high + low) // 2

            if checkCurrRate(currRate):
                validPrev = currRate
                high = currRate - 1
            else:
                low = currRate + 1
        
        return validPrev