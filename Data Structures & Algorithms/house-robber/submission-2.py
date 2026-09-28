class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [9, 1, 3, 8, 0]
            # 0, 2, 4 -> 12
            # 1, 3 -> 9
            # 0, 3 -> 17 (ANSWER)
        
        # Rules out skip by 1
        # Rules out skipping then backtracking

        # Recursive, three options
            # skip this one and rob next
            # skip next and rob this
            # max(recursive(i + 1), nums[i] + recursive (i + 2))
                # base case:
                    # check bounds
                    # visited
                        # store recursive(i) as a tuple
                            # (x, y) -> x is if you take curr, y is if you skip curr
        
        myMap = {}
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 0:
            return 0

        def dfs(index):
            if index < 0 or index >= n:
                return 0
            elif index in myMap:
                return max(myMap[index][0], myMap[index][1])

            myMap[index] = (dfs(index + 1), nums[index] + dfs(index + 2))
            return max(myMap[index][0], myMap[index][1])
        
        return dfs(0)