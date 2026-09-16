```python
from collections import deque


class Solution:
    def levelOrder(self, root):
        result = []

        # If the tree is empty
        if root is None:
            return result

        # Queue is used for level order traversal
        queue = deque([root])

        while queue:
            # Number of nodes in the current level
            level_size = len(queue)
            current_level = []

            # Process all nodes of the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Add left child
                if node.left:
                    queue.append(node.left)

                # Add right child
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
```
