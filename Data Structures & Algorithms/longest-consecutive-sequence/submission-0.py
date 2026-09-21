class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        num_set = set(nums)
        maxStreak = 0

        for num in num_set:
            if num - 1 not in num_set:
                currNum = num
                currStreak = 1

                while currNum + 1 in num_set:
                    currStreak += 1
                    currNum += 1

                if currStreak > maxStreak:
                    maxStreak = currStreak
        
        return maxStreak