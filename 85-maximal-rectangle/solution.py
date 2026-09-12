```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in range(rows):

            # Build histogram for the current row
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Find largest rectangle in the histogram
            stack = []

            for i in range(cols + 1):
                current_height = heights[i] if i < cols else 0

                while stack and heights[stack[-1]] > current_height:
                    height = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    area = height * width
                    max_area = max(max_area, area)

                stack.append(i)

        return max_area
```
