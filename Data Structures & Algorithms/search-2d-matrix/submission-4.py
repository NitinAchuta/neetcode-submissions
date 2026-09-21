class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bot = 0, len(matrix) - 1
        midIndex = -1

        # Find the actual row
        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                midIndex = mid
                break
        
        # Find the true value
        l, r = 0, len(matrix[midIndex]) - 1

        while l <= r:

            mid = (l + r) // 2
            if matrix[midIndex][mid] < target:
                l = mid + 1
            elif matrix[midIndex][mid] > target:
                r = mid - 1
            elif matrix[midIndex][mid] == target:
                return True
            else:
                return False
        return False


