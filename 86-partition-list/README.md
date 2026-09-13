# Partition List

## Problem

You are given the `head` of a linked list and a value `x`.

The task is to rearrange the linked list so that:

- All nodes with values **less than `x`** come first.
- All nodes with values **greater than or equal to `x`** come after them.
- The original relative order of nodes in both groups must be preserved.

### Example 1

**Input:**

```text
head = [1,4,3,2,5,2]
x = 3
```

**Output:**

```text
[1,2,2,4,3,5]
```

The nodes less than `3` are:

```text
1 → 2 → 2
```

The nodes greater than or equal to `3` are:

```text
4 → 3 → 5
```

Combining them:

```text
1 → 2 → 2 → 4 → 3 → 5
```

### Example 2

**Input:**

```text
head = [2,1]
x = 2
```

**Output:**

```text
[1,2]
```

---

## Approach

We create **two separate linked lists**:

### 1. Less-than List

Contains nodes where:

```text
node.val < x
```

### 2. Greater-or-equal List

Contains nodes where:

```text
node.val >= x
```

While traversing the original list, we add each node to the appropriate list.

Finally, we connect the two lists.

```text
Original List
      ↓
   Traverse
      ↓
 ┌───────────────┐
 │               │
 < x            >= x
 │               │
 ↓               ↓
Less List    Greater List
 │               │
 └───────┬───────┘
         ↓
      Combine
         ↓
   Final List
```

---

## Important Point: Preserve Relative Order

The problem says that the original relative order must be preserved.

For example:

```text
Input:
1 → 4 → 3 → 2 → 5 → 2
x = 3
```

Nodes less than `3` appear in the original order:

```text
1 → 2 → 2
```

Nodes greater than or equal to `3` also remain in their original order:

```text
4 → 3 → 5
```

So the result is:

```text
1 → 2 → 2 → 4 → 3 → 5
```

We **do not sort** the values.

---

## Algorithm

1. Create a dummy node for the `less` list.
2. Create a dummy node for the `greater` list.
3. Traverse the original linked list.
4. If the current node's value is less than `x`:
   - Add it to the `less` list.
5. Otherwise:
   - Add it to the `greater` list.
6. Continue until all nodes are processed.
7. Set the end of the greater list to `None`.
8. Connect the end of the less list to the beginning of the greater list.
9. Return the beginning of the less list.

---

## Dry Run

Consider:

```text
1 → 4 → 3 → 2 → 5 → 2
x = 3
```

### Start

```text
Less List:
empty

Greater List:
empty
```

### Process 1

Since:

```text
1 < 3
```

Add `1` to the less list.

```text
Less:
1
```

### Process 4

Since:

```text
4 >= 3
```

Add `4` to the greater list.

```text
Greater:
4
```

### Process 3

Since:

```text
3 >= 3
```

Add `3` to the greater list.

```text
Greater:
4 → 3
```

### Process 2

Since:

```text
2 < 3
```

Add `2` to the less list.

```text
Less:
1 → 2
```

### Process 5

Since:

```text
5 >= 3
```

Add `5` to the greater list.

```text
Greater:
4 → 3 → 5
```

### Process 2

Since:

```text
2 < 3
```

Add `2` to the less list.

```text
Less:
1 → 2 → 2
```

### Combine Both Lists

```text
Less:
1 → 2 → 2

Greater:
4 → 3 → 5
```

Join them:

```text
1 → 2 → 2 → 4 → 3 → 5
```

Therefore:

```text
Output = [1,2,2,4,3,5]
```

---

## How the Code Works

### Create Dummy Nodes

```python
less_dummy = ListNode(0)
greater_dummy = ListNode(0)
```

Dummy nodes make it easier to build the two lists without handling the first node separately.

### Create Pointers

```python
less = less_dummy
greater = greater_dummy
```

These pointers always point to the last node of their respective lists.

### Traverse the List

```python
current = head

while current:
```

We process every node exactly once.

### Add Smaller Nodes

```python
if current.val < x:
    less.next = current
    less = less.next
```

If the value is smaller than `x`, it is added to the less-than list.

### Add Greater-or-Equal Nodes

```python
else:
    greater.next = current
    greater = greater.next
```

Values equal to or greater than `x` are added to the second list.

### End the Second List

```python
greater.next = None
```

This is important because the original `next` pointers may still point to nodes from the original list.

We must explicitly terminate the greater list.

### Combine the Lists

```python
less.next = greater_dummy.next
```

The less-than list is connected to the greater-or-equal list.

---

## Why Use Two Dummy Nodes?

Without dummy nodes, we would need special conditions for the first node of each partition.

With dummy nodes:

```text
less_dummy → less nodes
greater_dummy → greater nodes
```

After building the lists, we simply return:

```python
less_dummy.next
```

The dummy nodes themselves are not part of the result.

---

## Important Edge Cases

### 1. Empty List

```text
Input:
[]

x = 3

Output:
[]
```

### 2. All Nodes Are Less Than `x`

```text
Input:
[1,2,2]

x = 5

Output:
[1,2,2]
```

### 3. All Nodes Are Greater Than or Equal to `x`

```text
Input:
[5,6,7]

x = 3

Output:
[5,6,7]
```

### 4. Nodes Equal to `x`

Nodes equal to `x` belong to the second partition.

```text
Input:
[1,3,2,3]

x = 3
```

Result:

```text
[1,2,3,3]
```

### 5. Relative Order

Input:

```text
[3,1,4,2,5]
x = 3
```

Smaller values:

```text
1 → 2
```

Greater or equal values:

```text
3 → 4 → 5
```

Result:

```text
1 → 2 → 3 → 4 → 5
```

The relative order within each group is preserved.

---

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

We traverse the linked list only once.

### Space Complexity

```text
O(1)
```

We only use a few pointers and dummy nodes.

The nodes themselves are rearranged; no new list of `n` nodes is created.

---

## Key Concept

The main concept used is:

**Linked List Partitioning**

We divide the original list into two parts:

```text
Nodes < x
      +
Nodes >= x
```

Then we join them while preserving their original relative order.

---

## Difference Between Partitioning and Sorting

This problem does **not** ask us to sort the linked list.

For example:

```text
Input:
1 → 5 → 2 → 4 → 3
x = 3
```

Partitioning gives:

```text
1 → 2 → 5 → 4 → 3
```

Notice that `5 → 4 → 3` is not sorted.

Only the partition condition matters:

```text
Values < 3:
1 → 2

Values >= 3:
5 → 4 → 3
```

Their original relative order is preserved.

---

## Constraints

- Number of nodes: `0 <= n <= 200`
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 86
- **Problem Name:** Partition List
- **Difficulty:** Medium
- **Topics:** Linked List, Two Pointers

---

## File Structure

```text
LeetCode_solution/
│
└── 86-partition-list/
    ├── README.md
    └── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/86-partition-list/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
