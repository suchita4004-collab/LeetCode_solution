```python
class Solution:
    def reverseBetween(self, head, left, right):
        # Dummy node helps when left = 1
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node just before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Start reversing from the left position
        current = prev.next

        # Reverse nodes one by one
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
```
