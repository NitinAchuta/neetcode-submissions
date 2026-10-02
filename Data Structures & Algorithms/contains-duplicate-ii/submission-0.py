class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mySet = set()
        L = 0 

        for R in range(len(nums)):
            if R - L> k:
                mySet.remove(nums[L])
                L += 1
            if nums[R] in mySet:
                return True
            mySet.add(nums[R])
        return False
        