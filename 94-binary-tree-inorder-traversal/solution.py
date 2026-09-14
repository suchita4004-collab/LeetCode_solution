```python```python
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            # Visit left subtree
            inorder(node.left)

            # Visit root
            result.append(node.val)

            # Visit right subtree
            inorder(node.right)

        inorder(root)

        return result
```

