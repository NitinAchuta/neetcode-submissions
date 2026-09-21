class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(r, c, v: set()) -> bool:
            """
            be a void return type
            increment count
            find every single part of that specific island
            """
            # check bounds -> if r < 0, if c < 0 -> -> return False
            # check to see if we've already visited -> if (r, c) in v -> return False
            # check to see if its a 1 if grid[r][c] == 0 -> return False
            if (min(r, c) < 0 or (r,c) in v or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return False

            # come here if all of those hold false
            v.add((r,c))
                # come back to how we'll increment the count
            dfs(r -1, c, v) # go up
            dfs(r + 1, c, v) # go down
            dfs(r, c - 1, v) # go left
            dfs(r, c + 1, v) # go right
            
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, visited):
                    count += 1

        return count


        