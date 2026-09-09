# 0061 - Rotate List

## Problem

Given the `head` of a linked list, rotate the list to the **right by `k` places**.

A right rotation moves the last node to the beginning of the list.

For example:

```text
[1,2,3,4,5]
```

After one rotation:

```text
[5,1,2,3,4]
```

After two rotations:

```text
[4,5,1,2,3]
```

## Examples

### Example 1

**Input:**
```text
head = [1,2,3,4,5]
k = 2
```

**Output:**
```text
[4,5,1,2,3]
```

### Example 2

**Input:**
```text
head = [0,1,2]
k = 4
```

**Output:**
```text
[2,0,1]
```

## Approach

We use the **Circular Linked List** approach.

Instead of rotating the linked list one step at a time, we first find:

- The length of the linked list.
- The last node.
- The position where the new list should start.

### Important Observation

If the linked list contains `n` nodes, rotating it `n` times produces the original list.

Therefore, we can reduce `k` using:

```text
k = k % n
```

For example:

```text
n = 3
k = 4

4 % 3 = 1
```

So rotating `[0,1,2]` four times is the same as rotating it once.

## Algorithm

1. If the list is empty, has only one node, or `k == 0`, return `head`.
2. Find the length of the linked list.
3. Find the last node (`tail`).
4. Calculate:
   ```text
   k = k % length
   ```
5. If `k == 0`, return the original list.
6. Connect the last node to the head to make the list circular.
7. Find the new tail.
8. The node after the new tail becomes the new head.
9. Break the circular connection.
10. Return the new head.

## Solution

```python
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

        # Reduce unnecessary rotations
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

        # Node after new tail becomes new head
        new_head = new_tail.next

        # Break the circular list
        new_tail.next = None

        return new_head
```

## Dry Run

Consider:

```text
head = [1,2,3,4,5]
k = 2
```

### Step 1: Find Length

```text
1 → 2 → 3 → 4 → 5
```

Length:

```text
5
```

### Step 2: Reduce `k`

```text
k = k % length
k = 2 % 5
k = 2
```

### Step 3: Make the List Circular

Connect the last node to the head:

```text
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

### Step 4: Find New Tail

For a right rotation by `k`, the new tail is at:

```text
length - k - 1
```

So:

```text
5 - 2 - 1 = 2
```

The node at index `2` is:

```text
3
```

Therefore:

```text
new_tail = 3
```

### Step 5: Find New Head

The node after `3` is:

```text
4
```

Therefore:

```text
new_head = 4
```

### Step 6: Break the Circular List

Set:

```text
3.next = None
```

Final list:

```text
4 → 5 → 1 → 2 → 3
```

Therefore:

```text
Output = [4,5,1,2,3]
```

## Why `k % length` Is Important

Suppose:

```text
head = [0,1,2]
k = 4
```

There are 3 nodes, so:

```text
4 % 3 = 1
```

Therefore, we only need to rotate once:

```text
[0,1,2]
     ↓
[2,0,1]
```

This avoids performing unnecessary rotations.

## Edge Cases

### Empty List

```text
head = []
```

Output:

```text
[]
```

### One Node

```text
head = [1]
k = 100
```

Output:

```text
[1]
```

### `k = 0`

```text
head = [1,2,3]
k = 0
```

Output:

```text
[1,2,3]
```

### `k` Is a Multiple of Length

```text
head = [1,2,3]
k = 3
```

Since:

```text
3 % 3 = 0
```

the list remains unchanged:

```text
[1,2,3]
```

## Complexity Analysis

Finding the length takes `O(n)` time.

Finding the new tail takes at most `O(n)` time.

Therefore:

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

The solution modifies the linked-list pointers directly and does not create another linked list.

## Key Concept

The main idea is to temporarily convert the linked list into a **circular linked list**.

```text
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

Then we find the correct position for the new head and break the circle.

This allows the rotation to be performed efficiently.

## Constraints

- The number of nodes is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Language

**Python**

## LeetCode Information

- **Problem Number:** 61
- **Problem Name:** Rotate List
- **Difficulty:** Medium
- **Topics:** Linked List, Two Pointers

## Solution Link

[LeetCode - Rotate List](https://leetcode.com/problems/rotate-list/)

## Repository Structure

```text
LeetCode_solution/
│
├── 0001-two-sum/
├── 0002-add-two-numbers/
├── ...
├── 0059-spiral-matrix-ii/
│   ├── README.md
│   └── solution.py
│
├── 0060-permutation-sequence/
│   ├── README.md
│   └── solution.py
│
└── 0061-rotate-list/
    ├── README.md
    └── solution.py
```

## Key Takeaway

A linked list can be rotated efficiently by:

```text
1. Finding its length
2. Reducing k using k % length
3. Making the list circular
4. Finding the new tail
5. Breaking the circle
```

This gives an efficient **O(n) time and O(1) extra space** solution.
