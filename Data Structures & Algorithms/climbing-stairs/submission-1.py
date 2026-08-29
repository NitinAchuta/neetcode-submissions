class Solution:
    prevs = {}

    def climbStairs(self, n: int) -> int:

        # f(n) = f(n-1) + f(n-2)
        # f(0) = 0
        # f(1) = 1
        if n < 0:
            return 0
        elif n <= 1:
            return 1

        if n in Solution.prevs:
            return Solution.prevs[n]
        else:
            Solution.prevs[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)


        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


        
        