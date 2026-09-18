# 109. Convert Sorted List to Binary Search Tree

**Difficulty:** Medium  
**Language:** Python

## Problem

Given the `head` of a singly linked list where the elements are sorted in **ascending order**, convert it into a **height-balanced Binary Search Tree (BST)**.

A height-balanced binary tree is a tree where the heights of the left and right subtrees of every node differ by at most 1.

## Examples

### Example 1

**Input:**

```text id="xq0z9a"
head = [-10,-3,0,5,9]
```

**Output:**

```text id="v5z8fh"
[0,-3,9,-10,null,5]
```

One possible tree is:

```text id="1f3c7m"
        0
       / \
     -3   9
     /   /
   -10   5
```

### Example 2

**Input:**

```text id="k2yq8p"
head = []
```

**Output:**

```text id="3m7x1c"
[]
```

## Approach

In the previous problem (#108), the input was a sorted array, so we could directly access the middle element using an index.

Here, the input is a **singly linked list**, so we cannot directly access the middle element.

To find the middle node, we use the **slow and fast pointer technique**.

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.
- When `fast` reaches the end, `slow` is at the middle.

The middle node becomes the root of the BST.

Then:

- Nodes before the middle become the left subtree.
- Nodes after the middle become the right subtree.
- We repeat the same process recursively.

## Algorithm

```text id="0m7n1s"
1. If the linked list is empty, return None.
2. Find the middle node using slow and fast pointers.
3. The middle node becomes the root.
4. Split the linked list at the middle node.
5. Recursively construct the left subtree from the left part.
6. Recursively construct the right subtree from the right part.
7. Return the root.
```

## Dry Run

For:

```text id="5v9x2k"
head = [-10,-3,0,5,9]
```

The linked list is:

```text id="r6h3pw"
-10 → -3 → 0 → 5 → 9
```

### Step 1: Find the Middle

Using slow and fast pointers:

```text id="3o8kzq"
slow → 0
```

So `0` becomes the root.

```text id="j2k8pn"
        0
       / \
```

The list is divided into:

```text id="n5q1wf"
Left:  -10 → -3
Right: 5 → 9
```

### Step 2: Build Left Subtree

For:

```text id="q1v5mk"
-10 → -3
```

The middle node is `-3`.

So:

```text id="f7k3xd"
        0
       /
     -3
     /
   -10
```

### Step 3: Build Right Subtree

For:

```text id="x8n2lc"
5 → 9
```

The middle node is `9`.

So:

```text id="e4p7zs"
        0
       / \
     -3   9
     /   /
   -10   5
```

The resulting BST can be represented as:

```text id="t9k4yw"
[0,-3,9,-10,null,5]
```

## How the Code Works

First, we check whether the list is empty:

```python id="h2f6rv"
if head is None:
    return None
```

Then we use two pointers:

```python id="y8c4qp"
slow = head
fast = head
```

`slow` moves one step:

```python id="b4v6cx"
slow = slow.next
```

while `fast` moves two steps:

```python id="a7m1dz"
fast = fast.next.next
```

When `fast` reaches the end, `slow` points to the middle node.

We save the previous node:

```python id="r5c8nk"
prev = None
```

This allows us to disconnect the left part of the list from the middle:

```python id="q6w3pt"
prev.next = None
```

Then the middle value becomes the root:

```python id="z9k2fh"
root = TreeNode(slow.val)
```

Finally, we recursively construct both subtrees:

```python id="u3p7xm"
root.left = self.sortedListToBST(head)
root.right = self.sortedListToBST(slow.next)
```

## Important Edge Cases

### 1. Empty list

```text id="q8n3sa"
head = []
```

There are no nodes, so we return:

```text id="j5m1vf"
[]
```

### 2. Single node

```text id="e2r7kc"
head = [1]
```

The only node becomes the root.

```text id="x6p4bn"
    1
```

### 3. Two nodes

```text id="a9w2ls"
head = [1,3]
```

Either valid height-balanced arrangement can be produced depending on which middle node is selected.

## Complexity Analysis

Let `n` be the number of nodes in the linked list.

### Time Complexity

```text id="c5q9hx"
O(n log n)
```

At every recursive level, finding the middle takes `O(n)` time, and the list is divided approximately in half.

There are approximately `O(log n)` levels.

Therefore:

```text id="f7x2mv"
O(n log n)
```

### Space Complexity

```text id="z4p8kd"
O(log n)
```

The recursion depth is `O(log n)` because the resulting tree is height-balanced.

## Key Concept

The important technique is the **Slow and Fast Pointer** method.

```text id="m3v7qa"
Slow → moves 1 step
Fast → moves 2 steps
```

When `Fast` reaches the end:

```text id="r8c2ye"
Slow → Middle
```

The middle node is selected as the root:

```text id="j1k6wp"
             Middle
             /    \
          Left    Right
```

This keeps the BST height-balanced.

## Difference from #108

### #108 — Sorted Array

We can directly find the middle using an index:

```text id="b6t3vz"
mid = (left + right) // 2
```

### #109 — Sorted Linked List

We cannot access the middle directly, so we use:

```text id="n2y7kc"
Slow Pointer + Fast Pointer
```

## Constraints

- Number of nodes is in the range `[0, 2 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`.

## LeetCode Information

- **Problem:** Convert Sorted List to Binary Search Tree
- **Problem Number:** 109
- **Difficulty:** Medium
- **Language:** Python

## File Structure

```text id="v8m2qd"
109-convert-sorted-list-to-binary-search-tree/
│
├── README.md
└── solution.py
```

## Solution

See [`solution.py`](solution.py) for the complete Python solution.

## Repository

**GitHub Repository:** `LeetCode_solution`
