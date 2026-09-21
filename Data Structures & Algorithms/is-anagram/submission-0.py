class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word1 = {}
        word2 = {}

        for letter in s:
            if letter not in word1:
                word1[letter] = 1
            else:
                word1[letter] += 1

        for letter in t:
            if letter not in word2:
                word2[letter] = 1
            else:
                word2[letter] += 1

        if word1 == word2:
            return True
        else:
            return False

        