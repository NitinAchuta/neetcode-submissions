class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])


        def memo(row, col, cache):
            if row == ROWS or col == COLS:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if cache[row][col] > 0:
                return cache[row][col]
            if row == ROWS - 1 and col == COLS - 1:
                return 1
        
            cache[row][col] = memo(row + 1, col, cache) + memo(row, col + 1, cache)
            return cache[row][col]
        
        return memo(0, 0, [[0] * COLS for i in range(ROWS)])
