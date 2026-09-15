```python
class Solution:
    def numTrees(self, n):
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)

        # There is one way to make an empty tree
        dp[0] = 1

        # Calculate answer for each number of nodes
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left_nodes = root - 1
                right_nodes = nodes - root

                dp[nodes] += dp[left_nodes] * dp[right_nodes]

        return dp[n]
```
