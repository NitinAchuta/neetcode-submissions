class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hash:
                return [hash[difference], index]
            hash[number] = index



        