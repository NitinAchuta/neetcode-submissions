class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mySet = set()
        maxS = 0

        l, r = 0, 0

        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
                r += 1
                maxS = max(maxS, r - l)
            else:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1

        return maxS
            
        