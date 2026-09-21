class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix) -1, len(matrix[0]) - 1

        top = 0
        bot = rows

        # Find the right row
        row = -1

        while top <= bot:
            mid = top + (bot - top) // 2

            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                row = mid
                break

        if row < 0:
            return False

        # Find the right element
        low = 0
        high = cols

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True
        return False        
