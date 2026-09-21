class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        DIFF = color - image[sr][sc] # 2 - 1 -> 1
        startColor = image[sr][sc] 

        def dfs(r, c, visited: set(), endColor, startColor):
            # Rules to end dfs
                # 1. make sure we are in bounds
                    # if min(r, c) < 0 -> return
                    # if r == ROWS -> return
                    # if c == COLS -> return
                # 2. Check to see if neighboring pixels match orig color of start
                    # if image[r][c] != color -> return
                # 3. Check to see if r, c already exists in the set
                    # if (r, c) in set -> return 
            if(min(r, c) < 0 
            or r == ROWS or c == COLS
            or image[r][c] != startColor
            or (r, c) in visited):
                return
            # update set by adding (r, c) -> visit.add((r, c))
            # update (r, c) to add DIFF -> image[r][c] += DIFF
            visited.add((r, c))
            image[r][c] += DIFF
            # DFS routes
            dfs(r - 1, c, visited, color, startColor)# go up           
            dfs(r, c - 1, visited, color, startColor)# go left
            dfs(r, c + 1, visited, color, startColor)# go right
            dfs(r + 1, c, visited, color, startColor) # go down

            visited.remove((r,c))
            return
        dfs(sr, sc, set(), color, startColor)
        return image

        