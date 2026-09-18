class Solution:
    def sortedListToBST(self, head):
        # Empty linked list
        if head is None:
            return None

        # Find the middle node using slow and fast pointers
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect the left half from the middle node
        if prev:
            prev.next = None

        # Middle node becomes the root
        root = TreeNode(slow.val)

        # If there was only one node
        if slow == head:
            return root

        # Build left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
