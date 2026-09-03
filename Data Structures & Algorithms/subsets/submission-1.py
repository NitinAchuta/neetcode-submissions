class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        l = len(nums)
        def dfs(i):
            if i >= l:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
            return
        dfs(0)
        return res
        