class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myDict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in myDict:
                return [myDict[diff], index]
            myDict[num] = index