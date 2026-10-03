class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float("inf")
        currSum = 0

        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                length = min(length, R-L + 1)
                currSum -= nums[L]
                L += 1
        
        if length == float("inf"):
            return 0
        return length