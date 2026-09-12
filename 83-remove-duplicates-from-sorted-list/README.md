# Remove Duplicates from Sorted List

## Problem

You are given the `head` of a **sorted linked list**.

The task is to remove duplicate values so that **each element appears only once**.

The final linked list should remain sorted.

### Example 1

**Input:**
```text
[1,1,2]
```

**Output:**
```text
[1,2]
```

### Example 2

**Input:**
```text
[1,1,2,3,3]
```

**Output:**
```text
[1,2,3]
```

---

## Approach

Because the linked list is already sorted, duplicate values will always be next to each other.

For example:

```text
1 → 1 → 2 → 3 → 3
    ↑
 duplicate
```

We compare the current node with the next node.

- If both values are the same, we remove the next node.
- If the values are different, we move to the next node.

We do not need an extra data structure.

---

## Algorithm

1. Start from the head of the linked list.
2. Store the current node in `current`.
3. Check whether `current.val` is equal to `current.next.val`.
4. If they are equal:
   - Skip the duplicate node using:
   ```python
   current.next = current.next.next
   ```
5. Otherwise, move `current` to the next node.
6. Continue until the end of the list.
7. Return `head`.

---

## Dry Run

Consider:

```text
1 → 1 → 2 → 3 → 3
```

### Step 1

Compare:

```text
1 == 1
```

Duplicate found.

Remove the second `1`:

```text
1 → 2 → 3 → 3
```

### Step 2

Compare:

```text
1 != 2
```

Move forward:

```text
    2 → 3 → 3
```

### Step 3

Compare:

```text
2 != 3
```

Move forward:

```text
        3 → 3
```

### Step 4

Compare:

```text
3 == 3
```

Duplicate found.

Remove the second `3`:

```text
1 → 2 → 3
```

Final output:

```text
[1,2,3]
```

---

## How the Code Works

### Initialize Current Node

```python
current = head
```

We start checking from the first node.

### Check for Duplicate

```python
if current.val == current.next.val:
```

Since the list is sorted, equal consecutive values mean that the next node is a duplicate.

### Remove Duplicate

```python
current.next = current.next.next
```

Suppose the list is:

```text
1 → 1 → 2
```

The first `1` points directly to `2`:

```text
1 ─────→ 2
```

So the duplicate node is skipped.

### Move Forward

```python
current = current.next
```

We only move forward when the current and next values are different.

---

## Why Does This Work?

The list is sorted, so all duplicate values are together.

For example:

```text
1 → 1 → 1 → 2 → 3 → 3
```

When we find the first `1`, we repeatedly remove the next duplicate:

```text
1 → 1 → 1 → 2
```

```text
1 → 1 → 2
```

```text
1 → 2
```

Therefore, only one occurrence of each value remains.

---

## Important Edge Cases

### 1. Empty List

```text
Input: []
Output: []
```

### 2. Single Node

```text
Input: [5]
Output: [5]
```

### 3. No Duplicates

```text
Input: [1,2,3]
Output: [1,2,3]
```

### 4. All Nodes Are Same

```text
Input: [2,2,2,2]
Output: [2]
```

### 5. Duplicates at Different Positions

```text
Input: [1,1,2,3,3]
Output: [1,2,3]
```

---

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

Each node is visited at most a few times.

### Space Complexity

```text
O(1)
```

We only use one pointer and modify the linked list directly.

---

## Key Concept

The main concept used is the **Two Consecutive Nodes Comparison**.

Since the list is sorted:

```text
current.val == current.next.val
```

means that `current.next` is a duplicate.

We simply skip that node.

---

## Difference from LeetCode #82

This problem is different from **#82 – Remove Duplicates from Sorted List II**.

### #82

All occurrences of a duplicated value are removed.

```text
Input: 1 → 2 → 2 → 3
Output: 1 → 3
```

### #83

Duplicates are removed, but **one copy is kept**.

```text
Input: 1 → 2 → 2 → 3
Output: 1 → 2 → 3
```

---

## Constraints

- Number of nodes: `0 <= n <= 300`
- `-100 <= Node.val <= 100`
- The linked list is sorted in ascending order.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 83
- **Problem Name:** Remove Duplicates from Sorted List
- **Difficulty:** Easy
- **Topic:** Linked List

---

## File Structure

```text
LeetCode_solution/
│
└── 83-remove-duplicates-from-sorted-list/
    ├── README.md
    └── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/83-remove-duplicates-from-sorted-list/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
