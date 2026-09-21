class Solution:
    def isPalindrome(self, s: str) -> bool:

        myStr = ""

        for val in s:
            if val.isalnum():
                myStr += val.lower()

        return myStr == myStr[::-1]

        