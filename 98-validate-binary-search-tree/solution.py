```python
class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True

            # Current node must be strictly between low and high
            if node.val <= low or node.val >= high:
                return False

            # Check left and right subtrees
            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))
```
