class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        # Step 1: Create a copy of every node
        old_to_new = {}

        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random pointers
        current = head

        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next

        # Step 3: Return copied head
        return old_to_new[head]