class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next
