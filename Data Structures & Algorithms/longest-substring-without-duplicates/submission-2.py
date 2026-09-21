class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxSubstring = 0
        longestSet = set()
        l = 0

        for letter in s:
            while letter in longestSet:
                longestSet.remove(s[l])
                l += 1
            longestSet.add(letter)
            maxSubstring = max(maxSubstring, len(longestSet))
        
        return maxSubstring


