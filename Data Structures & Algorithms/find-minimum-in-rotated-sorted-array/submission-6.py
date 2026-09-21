class Solution:
    def findMin(self, nums: List[int]) -> int:


        left, right = 0, len(nums) - 1
        res = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            
            middle = left + (right - left) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return res

        