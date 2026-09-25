class Solution:
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        current = head

        while current:
            next_node = current.next

            # Find the position for current node
            prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current node
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next