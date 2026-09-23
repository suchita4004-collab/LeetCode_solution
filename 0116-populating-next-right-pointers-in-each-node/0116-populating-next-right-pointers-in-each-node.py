class Solution:
    def connect(self, root):
        if root is None:
            return None

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to next node's left child
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root