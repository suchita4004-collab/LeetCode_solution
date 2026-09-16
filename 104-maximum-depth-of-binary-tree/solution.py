```python
class Solution:
    def maxDepth(self, root):
        # Empty tree has depth 0
        if root is None:
            return 0

        # Find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Take the larger depth and add the current node
        return 1 + max(left_depth, right_depth)
