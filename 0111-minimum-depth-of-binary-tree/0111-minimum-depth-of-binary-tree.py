from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # First leaf found is the minimum depth
            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return 0