class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        l1, l2 = len(text1), len(text2) #l1 = rows, l2 = cols
        if text1 == text2:
            return l1

        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

        for row in range(l1 - 1, -1, -1):
            for col in range(l2 - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]
