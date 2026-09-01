class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        # dp[i][j] means:
        # first i characters of s match first j characters of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Normal character or '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # '*'
                elif p[j - 1] == '*':
                    # Option 1: '*' matches zero occurrences
                    dp[i][j] = dp[i][j - 2]

                    # Option 2: '*' matches one or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
