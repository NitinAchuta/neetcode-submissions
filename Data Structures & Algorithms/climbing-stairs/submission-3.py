class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def memoization(n):
            
            if n in memo:
                return memo[n]
            elif n == 0:
                return 1
            elif n < 0:
                return 0
            
            memo[n] = memoization(n-1) + memoization(n - 2)
            return memo[n]

        memoization(n)
        return memo[n]