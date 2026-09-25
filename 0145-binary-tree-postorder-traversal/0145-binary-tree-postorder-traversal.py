class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        result.reverse()
        return result