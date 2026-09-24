class Solution:
    def minCut(self, s):
        n = len(s)

        # palindrome[i][j] = True if s[i:j+1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        # dp[i] = minimum cuts needed for s[0:i+1]
        dp = [0] * n

        for i in range(n):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i

                for j in range(1, i + 1):
                    if palindrome[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]