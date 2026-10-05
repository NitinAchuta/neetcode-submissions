class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mySet = set()
        L = 0
        maxLen = 0

        for R in range(len(s)):
            if s[R] in mySet:
                while s[R] in mySet:
                    mySet.remove(s[L])
                    L += 1
            mySet.add(s[R])
            maxLen = max(maxLen, R - L + 1)
        return maxLen
        