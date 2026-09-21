class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right

        def dfs(r, c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0

            count = 1
            grid[r][c] = 0 # mark it as complete to not double count

            for dr, dc in DIRS:
                count += dfs(r + dr, c + dc)

            return count


        for r in range(ROWS):
            for c in range(COLS):
                currArea = dfs(r, c)
                maxArea = max(currArea, maxArea)

        return maxArea

        # iterate through every element on the grid
            # run dfs
            # update maxArea        