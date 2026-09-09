class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Avoid unnecessary rotations
        k %= length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # New head is after new tail
        new_head = new_tail.next

        # Break the circular list
        new_tail.next = None

        return new_head
