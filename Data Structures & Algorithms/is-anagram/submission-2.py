class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word1 = {}
        word2 = {}

        for letter in s:
            word1[letter] = 1 + word1.get(letter, 0)

        for letter in t:
            word2[letter] = 1 + word2.get(letter, 0)

        if word1 == word2:
            return True
        else:
            return False

        