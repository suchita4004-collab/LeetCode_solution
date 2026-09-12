```python
class Solution:
    def deleteDuplicates(self, head):
        # Create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            # Check if the current node has duplicates
            if current.next and current.val == current.next.val:
                value = current.val

                # Skip all nodes having the same value
                while current and current.val == value:
                    current = current.next

                # Connect previous distinct node to the next distinct node
                prev.next = current

            else:
                # Current node is distinct, so move prev forward
                prev = current
                current = current.next

        return dummy.next
```
