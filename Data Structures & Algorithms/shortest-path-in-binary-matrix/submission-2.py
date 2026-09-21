class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0, 0))
        length = 0
        DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while queue:
            length += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (
                    r < 0 or c < 0 or r >= ROWS or c >= ROWS
                    or (r, c) in visited or grid[r][c] != 0
                ):
                    continue
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                visited.add((r, c))
                for dr, dc in DIRS:
                    queue.append((r + dr, c + dc))
        return -1



        