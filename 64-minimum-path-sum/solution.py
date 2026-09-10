```python
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Update first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Update first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Calculate minimum path sum
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
```
