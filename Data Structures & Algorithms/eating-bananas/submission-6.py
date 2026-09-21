class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Helper function to to see if curr rate works
        def checkCurrRate(rate, piles = piles, h = h):
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(float(pile) / rate)
                if totalTime > h:
                    return False
            return True
        
        low, high = 1, max(piles)
        validPrev = 0

        while low <= high:
            mid = (high + low) // 2

            if checkCurrRate(mid):
                high = mid - 1
                validPrev = mid
            else:
                low = mid + 1
        return validPrev
        
        