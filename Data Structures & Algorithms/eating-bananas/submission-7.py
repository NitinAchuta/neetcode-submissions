import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        maxBananas = max(piles)
        currMin = None

        L, R = 1, maxBananas
        while L <= R:
            mid = (L + R) // 2
            
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            
            if t > h:
                L = mid + 1
            else:
                currMin = mid
                R = mid - 1
        return currMin




        