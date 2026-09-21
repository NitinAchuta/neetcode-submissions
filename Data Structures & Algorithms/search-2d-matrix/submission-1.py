class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find the row

        low = 0
        high = len(matrix) - 1
        row = -1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                row = mid
                break
                
        if row == -1:
            return False

        # Find the right item in that row

        low = 0
        high = len(matrix[row]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[row][mid] < target:
                low = mid + 1
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                return True

        return False