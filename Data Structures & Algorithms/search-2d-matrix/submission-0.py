class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1

        # Search the correct row
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break  # target is in this row

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, cols - 1

        # Search within the row
        while l <= r:
            middle = (l + r) // 2
            if target > matrix[row][middle]:
                l = middle + 1
            elif target < matrix[row][middle]:
                r = middle - 1
            else:
                return True

        return False
