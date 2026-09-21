class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0, 0, 1)])
        visit = set()
        visit.add((0, 0))
        DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1],
                [1, 1], [1, -1], [-1, 1], [1, -1]]
                
        while queue:
            for i in range(len(queue)):
                r, c, length = queue.popleft()
                if min(r, c) < 0 or max(r, c) >= ROWS or grid[r][c]:
                    continue
                if r == ROWS - 1 and c == COLS - 1:
                    return length 
                
                for dr, dc in DIRS:
                    if (r+dr, c+dc) not in visit:
                        queue.append((r+dr,c+dc,length+1))
                        visit.add((r+dr,c+dc))

        return -1

