```python
class Solution:
    def isSameTree(self, p, q):
        # If both nodes are empty, they are the same
        if p is None and q is None:
            return True

        # If one node is empty and the other is not
        if p is None or q is None:
            return False

        # Values must be equal
        if p.val != q.val:
            return False

        # Check left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
```
