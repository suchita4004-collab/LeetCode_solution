class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        length = m + n - 1

        if length % 2 == 1:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current = dp[i][j]

                if i > 0:
                    for balance in dp[i - 1][j]:
                        if grid[i][j] == '(':
                            current.add(balance + 1)
                        elif balance > 0:
                            current.add(balance - 1)

                if j > 0:
                    for balance in dp[i][j - 1]:
                        if grid[i][j] == '(':
                            current.add(balance + 1)
                        elif balance > 0:
                            current.add(balance - 1)

        return 0 in dp[m - 1][n - 1]