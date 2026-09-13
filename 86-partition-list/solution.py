```python
class Solution:
    def partition(self, head, x):
        # Dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        current = head

        while current:
            if current.val < x:
                # Add node to the less-than partition
                less.next = current
                less = less.next
            else:
                # Add node to the greater-than-or-equal partition
                greater.next = current
                greater = greater.next

            current = current.next

        # End the greater partition
        greater.next = None

        # Join both partitions
        less.next = greater_dummy.next

        return less_dummy.next
```
