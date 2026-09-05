class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mySet = set()

        for i in range(len(nums)):
            if target - nums[i] in mySet:
                return [nums.index(target-nums[i]), i]
            mySet.add(nums[i])
        
        return [-1, -1]
        