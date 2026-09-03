class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        l = len(nums)
        def dfs(i, acc: List[int]):
            if i >= l:
                res.append(acc[::])
                return
            curr = nums[i]
            print(curr)

            acc.append(curr)
            dfs(i + 1, acc)
            acc.pop()
            dfs(i + 1, acc)
            return

        if not nums:
            return res
        dfs(0, [])
        return res
