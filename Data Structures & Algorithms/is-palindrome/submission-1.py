class Solution:
    def isPalindrome(self, s: str) -> bool:

        myStr = ""

        for l in s:
            if l.isalnum():
                myStr += l.lower()
        
        return myStr == myStr[::-1]
        