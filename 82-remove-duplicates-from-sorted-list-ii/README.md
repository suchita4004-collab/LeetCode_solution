# Remove Duplicates from Sorted List II

## Problem

You are given the `head` of a **sorted linked list**.

The task is to remove **all nodes that have duplicate values**.

Only values that appear **exactly once** should remain in the linked list.

The final linked list should also remain sorted.

### Example 1

**Input:**
```text
head = [1,2,3,3,4,4,5]
```

**Output:**
```text
[1,2,5]
```

### Example 2

**Input:**
```text
head = [1,1,1,2,3]
```

**Output:**
```text
[2,3]
```

---

## Approach

Since the linked list is already sorted, duplicate values will always be next to each other.

For example:

```text
1 → 2 → 3 → 3 → 4 → 4 → 5
        ↑────↑   ↑────↑
       duplicate duplicate
```

We can use three main ideas:

- `dummy` node – placed before the head.
- `prev` – points to the last node that is definitely distinct.
- `current` – checks the current nodes.

Whenever a duplicate is found, we skip **all nodes with that value**.

---

## Why Do We Need a Dummy Node?

A duplicate can occur at the beginning of the list.

For example:

```text
1 → 1 → 2 → 3
```

Both `1`s have to be removed.

Using a dummy node makes it easy to change the head:

```text
dummy → 1 → 1 → 2 → 3
```

After removing the duplicate:

```text
dummy → 2 → 3
```

Finally, we return:

```text
dummy.next
```

---

## Algorithm

1. Create a dummy node before the head.
2. Set `prev` to the dummy node.
3. Set `current` to the head.
4. Traverse the linked list.
5. If `current` and `current.next` have the same value:
   - Store the duplicate value.
   - Skip all nodes having that value.
   - Connect `prev.next` to the first different node.
6. Otherwise:
   - Move `prev` to `current`.
   - Move `current` to the next node.
7. Return `dummy.next`.

---

## Dry Run

Consider:

```text
1 → 2 → 3 → 3 → 4 → 4 → 5
```

### Step 1

`1` is not duplicated.

```text
prev = 1
current = 2
```

### Step 2

`2` is not duplicated.

```text
prev = 2
current = 3
```

### Step 3

We find:

```text
3 → 3
```

So `3` is duplicated.

Skip both `3`s:

```text
1 → 2 → 4 → 4 → 5
```

### Step 4

We find:

```text
4 → 4
```

So `4` is also duplicated.

Skip both `4`s:

```text
1 → 2 → 5
```

### Step 5

`5` is distinct.

Final result:

```text
1 → 2 → 5
```

Therefore:

```text
Output = [1,2,5]
```

---

## How the Code Works

### Create Dummy Node

```python
dummy = ListNode(0)
dummy.next = head
```

The dummy node makes it easier to remove duplicate nodes from the beginning.

### Initialize Pointers

```python
prev = dummy
current = head
```

- `prev` points to the last distinct node.
- `current` is used to examine the list.

### Detect Duplicate

```python
if current.next and current.val == current.next.val:
```

If the current node and next node have the same value, a duplicate exists.

### Skip All Duplicates

```python
value = current.val

while current and current.val == value:
    current = current.next
```

This removes **every occurrence** of that duplicate value.

### Connect the List

```python
prev.next = current
```

The previous distinct node is connected directly to the next distinct node.

---

## Important Edge Cases

### 1. Empty List

```text
Input: []
Output: []
```

### 2. No Duplicates

```text
Input: [1,2,3]
Output: [1,2,3]
```

### 3. All Nodes Are Duplicates

```text
Input: [1,1,2,2]
Output: []
```

### 4. Duplicate at the Beginning

```text
Input: [1,1,2,3]
Output: [2,3]
```

### 5. Three or More Duplicates

```text
Input: [1,2,2,2,3]
Output: [1,3]
```

All occurrences of `2` are removed.

---

## Complexity Analysis

Let `n` be the number of nodes in the linked list.

### Time Complexity

```text
O(n)
```

Each node is visited at most a constant number of times.

### Space Complexity

```text
O(1)
```

Only a few pointers are used. No extra list or data structure is required.

---

## Key Concept

The main concept used in this problem is:

**Two-Pointer Technique + Dummy Node**

Because the linked list is sorted, duplicate values are adjacent. This allows us to identify and remove duplicates efficiently in one traversal.

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

- **Problem Number:** 82
- **Problem Name:** Remove Duplicates from Sorted List II
- **Difficulty:** Medium
- **Topic:** Linked List, Two Pointers

---

## File Structure

```text
LeetCode_solution/
│
└── 82-remove-duplicates-from-sorted-list-ii/
    ├── README.md
    └── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/82-remove-duplicates-from-sorted-list-ii/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
