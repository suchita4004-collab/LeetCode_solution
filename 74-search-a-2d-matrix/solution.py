```python id="x5n4qk"
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        # Treat the matrix as one sorted array
        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D row and column
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
