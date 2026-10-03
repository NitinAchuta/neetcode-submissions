class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        myHash = {}
        res = 0
        L = 0
        maxF = 0

        for R in range(len(s)):
            myHash[s[R]] = 1 + myHash.get(s[R], 0)
            maxF = max(maxF, myHash[s[R]])

            while (R - L + 1) - maxF > k:
                myHash[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
            
        return res