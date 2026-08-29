class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # bSearch rows.
        #     compare target with 0 and n - 1 indices of that row
        #     if its in between, we found our row
        #     if 0 and n-1 are larger, bring pointer two down
        #     if 0 and n-1 are smaller, bring pointer one up
        # bSearch row for the actual index

        T, B = 0, len(matrix) - 1
        row = None
        n = len(matrix[0]) - 1
        while T <= B:
            mid = (T + B) // 2

            if matrix[mid][0] > target and matrix[mid][n] > target:
                B = mid - 1
            elif matrix[mid][0] < target and matrix[mid][n] < target:
                T = mid + 1
            else:
                row = mid
                break
                
        if row == None:
            return False

        L, R = 0, n

        while L <= R:
            mid = (L + R) // 2

            if matrix[row][mid] > target:
                R = mid - 1
            elif matrix[row][mid] < target:
                L = mid + 1
            else:
                return True
        return False


        