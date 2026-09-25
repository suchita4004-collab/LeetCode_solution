class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # Step 1: Find the middle of the list
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Step 3: Merge the two halves
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next