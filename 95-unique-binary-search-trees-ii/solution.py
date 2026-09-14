```python
class Solution:
    def generateTrees(self, n):
        def build(start, end):
            trees = []

            # No nodes in this range
            if start > end:
                return [None]

            # Try every value as the root
            for root_value in range(start, end + 1):

                # Generate all possible left subtrees
                left_trees = build(start, root_value - 1)

                # Generate all possible right subtrees
                right_trees = build(root_value + 1, end)

                # Combine every left subtree with every right subtree
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_value)
                        root.left = left
                        root.right = right

                        trees.append(root)

            return trees

        return build(1, n)
```
