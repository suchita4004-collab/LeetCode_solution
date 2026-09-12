```python
class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            # If two consecutive nodes have the same value
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head
```
