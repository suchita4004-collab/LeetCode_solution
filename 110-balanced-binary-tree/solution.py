class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0

            # Get height of left subtree
            left = height(node.left)
            if left == -1:
                return -1

            # Get height of right subtree
            right = height(node.right)
            if right == -1:
                return -1

            # Check if current node is balanced
            if abs(left - right) > 1:
                return -1

            # Return height of current subtree
            return 1 + max(left, right)

        return height(root) != -1
