class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for index, val in enumerate(nums):
            if target - val in myMap:
                return [myMap[target-val], index]
            myMap[val] = index
        