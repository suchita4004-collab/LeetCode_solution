class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if it is a leaf node
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])  # Copy path
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])

        return result
        