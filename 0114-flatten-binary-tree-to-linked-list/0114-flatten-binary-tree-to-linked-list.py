class Solution:
    def flatten(self, root):
        if root is None:
            return

        current = root

        while current:
            if current.left:
                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None

            current = current.right