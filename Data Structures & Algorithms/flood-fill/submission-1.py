class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        startColor = image[sr][sc] 

        if startColor == color:
            return image
        def dfs(r, c):
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
            or image[r][c] != startColor):
                return
            # update set by adding (r, c) -> visit.add((r, c))
            # update (r, c) to add DIFF -> image[r][c] += DIFF
            image[r][c] = color
            # DFS routes
            dfs(r - 1, c)# go up           
            dfs(r, c - 1)# go left
            dfs(r, c + 1)# go right
            dfs(r + 1, c) # go down

            return
        dfs(sr, sc)
        return image

        