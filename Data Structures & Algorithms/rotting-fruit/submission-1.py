class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        totalCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    totalCount += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))

        if totalCount == 0:
            return 0

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mins = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 
                    totalCount -= 1
                    if totalCount == 0:
                        return mins + 1
                    queue.append((nr, nc, mins + 1))

        return -1