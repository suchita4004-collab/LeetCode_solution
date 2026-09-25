class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        second = slow.next
        slow.next = None

        # Step 2: Sort both halves
        left = self.sortList(head)
        right = self.sortList(second)

        # Step 3: Merge the sorted halves
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next
        