class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mySet:
                return [mySet[diff], i]
            mySet[nums[i]] = i


        