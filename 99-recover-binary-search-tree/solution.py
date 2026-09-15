```python
class Solution:
    def recoverTree(self, root):
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev

            if node is None:
                return

            # Visit left subtree
            inorder(node.left)

            # Find incorrect order
            if prev and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            prev = node

            # Visit right subtree
            inorder(node.right)

        # Inorder traversal of a valid BST is sorted
        inorder(root)

        # Swap the values of the two incorrect nodes
        first.val, second.val = second.val, first.val
```
