class Solution:
    def sumNumbers(self, root):
        def dfs(node, current_number):
            if node is None:
                return 0

            current_number = current_number * 10 + node.val

            # Leaf node
            if node.left is None and node.right is None:
                return current_number

            return dfs(node.left, current_number) + dfs(node.right, current_number)

        return dfs(root, 0)
        