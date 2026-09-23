class Solution:
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            # Go backwards so we don't overwrite
            # values needed for the current iteration
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]