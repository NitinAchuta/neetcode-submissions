class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        l = len(nums)
        subset = []

        def dfs(i, total):                
            if total == target:
                res.append(subset.copy())
                return
            elif total > target:
                return
            if i >= l:
                return

            curr = nums[i]
            subset.append(curr)
            # dfs(i + 1, curr + total)
            dfs(i, curr + total)
            subset.pop()
            dfs(i + 1, total)
            return
        dfs(0, 0)
        return res
        