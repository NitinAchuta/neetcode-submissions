class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for i in range(9):
            res = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in res:
                    return False
                res.add(board[i][j])

        for i in range(9):
            res = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in res:
                    return False
                res.add(board[j][i])

        for i in range(9):
            res = set()
            row = 3*(i//3)
            col = 3*(i%3)
            for j in range(3):
                for k in range(3):
                    if board[j + row][k + col] == ".":
                        continue
                    if board[j + row][k + col] in res:
                        return False
                    res.add(board[j+row][k+col])   

        return True                 
                    



            

        