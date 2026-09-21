class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        res = 0
        mySet = set()

        while r < len(s):

            if s[r] not in mySet:
                mySet.add(s[r])
                res = max(res, len(mySet))
                r += 1
            else:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1
        
        return res


        