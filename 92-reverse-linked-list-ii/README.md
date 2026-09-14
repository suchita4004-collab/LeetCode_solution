```markdown
# 92. Reverse Linked List II

**Difficulty:** Medium  
**Language:** Python

## Problem

Given the head of a singly linked list and two positions `left` and `right`, reverse the nodes between these two positions.

The positions are counted starting from `1`.

The part of the list before `left` and the part after `right` should remain unchanged.

Return the modified linked list.

---

## Examples

### Example 1

```text
Input:
head = [1,2,3,4,5]
left = 2
right = 4

Output:
[1,4,3,2,5]
```

The original list is:

```text
1 → 2 → 3 → 4 → 5
```

We reverse the nodes from position `2` to position `4`:

```text
2 → 3 → 4
```

After reversing:

```text
4 → 3 → 2
```

Final list:

```text
1 → 4 → 3 → 2 → 5
```

---

### Example 2

```text
Input:
head = [5]
left = 1
right = 1

Output:
[5]
```

There is only one node, so there is nothing to reverse.

---

## Approach

We use **pointer manipulation** to reverse the required part of the linked list.

We do not create another linked list.

A dummy node is used before the head so that the same logic works even when `left = 1`.

We use a pointer called `prev` to reach the node just before the section that needs to be reversed.

Then we repeatedly move the next node to the front of the reversing section.

---

## Visual Representation

For:

```text
head = [1,2,3,4,5]
left = 2
right = 4
```

Initially:

```text
1 → 2 → 3 → 4 → 5
    ↑       ↑
  left    right
```

After reversal:

```text
1 → 4 → 3 → 2 → 5
```

The nodes outside the selected range remain unchanged.

---

## Algorithm

1. Create a dummy node before `head`.
2. Set `prev = dummy`.
3. Move `prev` to the node immediately before position `left`.
4. Set `current = prev.next`.
5. Repeat `right - left` times:
   - Store the node after `current`.
   - Remove that node from its current position.
   - Insert it immediately after `prev`.
6. Return `dummy.next`.

---

## Code

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

---

## Dry Run

Consider:

```text
head = [1,2,3,4,5]
left = 2
right = 4
```

Initial list:

```text
1 → 2 → 3 → 4 → 5
```

The node before position `2` is:

```text
1
```

So:

```text
prev = 1
current = 2
```

---

### Step 1

Move node `3` before node `2`.

```text
1 → 3 → 2 → 4 → 5
```

Now:

```text
current = 2
```

---

### Step 2

Move node `4` before node `3`.

```text
1 → 4 → 3 → 2 → 5
```

We have reached the required position.

Final result:

```text
[1,4,3,2,5]
```

---

## How the Pointer Manipulation Works

The important part is:

```python
next_node = current.next
```

This saves the node that we want to move.

Then:

```python
current.next = next_node.next
```

removes `next_node` from its current position.

Next:

```python
next_node.next = prev.next
```

connects it before the current reversed section.

Finally:

```python
prev.next = next_node
```

puts the node immediately after `prev`.

So the process is:

```text
Remove → Move → Insert
```

---

## Example of Pointer Movement

Before:

```text
1 → 2 → 3 → 4 → 5
    ↑   ↑
  prev current
```

Move `3`:

```text
1 → 3 → 2 → 4 → 5
    ↑
   prev
```

Move `4`:

```text
1 → 4 → 3 → 2 → 5
```

The selected section has been reversed.

---

## Why Use a Dummy Node?

We create:

```python
dummy = ListNode(0)
dummy.next = head
```

So the list becomes:

```text
dummy → 1 → 2 → 3 → 4 → 5
```

This is useful when:

```text
left = 1
```

because there is no actual node before the head.

The dummy node gives us a safe starting point.

---

## One-Pass Solution

The follow-up asks:

> Could you do it in one pass?

Yes.

The solution above performs the reversal while traversing the required part of the linked list and does not need a second traversal to reverse it.

The overall time complexity is:

```text
O(n)
```

where `n` is the number of nodes in the list.

---

## Important Edge Cases

### 1. Only One Node

```text
Input:
[5], left = 1, right = 1

Output:
[5]
```

No reversal is required.

---

### 2. `left` and `right` Are the Same

```text
Input:
[1,2,3], left = 2, right = 2

Output:
[1,2,3]
```

Only one node is selected.

---

### 3. Reverse From the Beginning

```text
Input:
[1,2,3,4], left = 1, right = 3

Output:
[3,2,1,4]
```

The dummy node makes this case easy to handle.

---

### 4. Reverse the Entire List

```text
Input:
[1,2,3,4,5], left = 1, right = 5

Output:
[5,4,3,2,1]
```

---

### 5. Reverse the Last Part

```text
Input:
[1,2,3,4,5], left = 3, right = 5

Output:
[1,2,5,4,3]
```

---

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

We traverse the list at most once.

### Space Complexity

```text
O(1)
```

Only a few pointers are used.

No extra list or array is created.

---

## Key Concept

The main idea is:

> **Take each node from the selected section and move it to the front of that section.**

For example:

```text
2 → 3 → 4
```

becomes:

```text
4 → 3 → 2
```

while the rest of the list remains unchanged.

---

## Constraints

- The number of nodes is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

---

## LeetCode Information

- **Problem:** 92. Reverse Linked List II
- **Difficulty:** Medium
- **Language:** Python
- **Topics:** Linked List, Two Pointers

---

## File Structure

```text
92-reverse-linked-list-ii/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/92-reverse-linked-list-ii/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
