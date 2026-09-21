class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         mySet = set(nums)
         return not(len(mySet) == len(nums))