```markdown
# 99. Recover Binary Search Tree

**Difficulty:** Medium  
**Language:** Python

---

## Problem

You are given the root of a Binary Search Tree (BST).

Exactly two nodes in the tree were swapped by mistake.

Your task is to recover the BST without changing its structure.

Only the values of the two incorrect nodes need to be swapped back.

---

## Examples

### Example 1

**Input:**
```text
root = [1,3,null,null,2]
```

**Output:**
```text
[3,1,null,null,2]
```

**Explanation:**

The value `3` cannot be the left child of `1` because `3 > 1`.

Swapping `1` and `3` makes the tree a valid BST.

---

### Example 2

**Input:**
```text
root = [3,1,4,null,null,2]
```

**Output:**
```text
[2,1,4,null,null,3]
```

**Explanation:**

The value `2` cannot be in the right subtree of `3` because `2 < 3`.

Swapping `2` and `3` makes the BST valid.

---

## Approach

The important property of a BST is:

> **Inorder traversal of a valid BST gives values in sorted order.**

For example:

```text
        3
       / \
      1   4
         /
        2
```

Inorder traversal:

```text
1 → 3 → 2 → 4
```

This is not sorted because:

```text
3 > 2
```

So, `3` and `2` are the two incorrect nodes.

### Steps

1. Perform an inorder traversal.
2. Keep track of the previous node.
3. If `prev.val > current.val`, we found an incorrect order.
4. Store the first incorrect node.
5. Keep updating the second incorrect node.
6. After traversal, swap the values of the two incorrect nodes.

---

## Algorithm

```text
first = None
second = None
prev = None

Perform inorder traversal:

    Visit left subtree

    If previous node exists and:
        previous.val > current.val

        If first is None:
            first = previous

        second = current

    Set previous = current

    Visit right subtree

Finally:
    swap first.val and second.val
```

---

## Dry Run

Consider:

```text
        3
       / \
      1   4
         /
        2
```

Inorder traversal:

```text
1 → 3 → 2 → 4
```

### Step 1

Compare:

```text
1 < 3
```

Correct.

### Step 2

Compare:

```text
3 > 2
```

Incorrect order found.

So:

```text
first = 3
second = 2
```

### Step 3

Compare:

```text
2 < 4
```

No problem.

### Step 4

Swap the values:

```text
3 ↔ 2
```

Tree becomes:

```text
        2
       / \
      1   4
         /
        3
```

Now the inorder traversal is:

```text
1 → 2 → 3 → 4
```

which is sorted, so the BST is recovered.

---

## How the Code Works

### 1. Initialize variables

```python
first = second = prev = None
```

- `first` stores the first incorrect node.
- `second` stores the second incorrect node.
- `prev` stores the previous node during inorder traversal.

### 2. Perform inorder traversal

```python
inorder(node.left)
```

We first visit the left subtree.

### 3. Find incorrect order

```python
if prev and prev.val > node.val:
```

In a valid BST, inorder values must be increasing.

If:

```text
previous value > current value
```

then the BST has an incorrect pair.

### 4. Store incorrect nodes

```python
if first is None:
    first = prev

second = node
```

The first incorrect node is stored only once.

The second node is updated whenever another incorrect order is found.

This handles both adjacent and non-adjacent swapped nodes.

### 5. Swap values

```python
first.val, second.val = second.val, first.val
```

Only the values are changed.

The tree structure remains unchanged.

---

## Important Edge Cases

### 1. Two adjacent nodes are swapped

Example:

```text
3 → 2
```

Only one incorrect pair is detected.

### 2. Two non-adjacent nodes are swapped

Example:

```text
1 → 5 → 3 → 4 → 2 → 6
```

There can be two incorrect positions.

The algorithm correctly identifies both nodes.

### 3. Negative values

BST values can be negative, so the solution does not make any assumption that values are positive.

### 4. Minimum number of nodes

The tree contains at least two nodes according to the constraints.

---

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

Every node is visited once during inorder traversal.

### Space Complexity

```text
O(h)
```

where `h` is the height of the tree.

The recursive inorder traversal uses the call stack.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```

---

## Constraints

- Number of nodes is in the range `[2, 1000]`.
- `-2^31 <= Node.val <= 2^31 - 1`
- Exactly two nodes are swapped.
- The tree structure must not be changed.

---

## Key Concept

The main idea is:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Order
 ↓
Find violations
 ↓
Identify two incorrect nodes
 ↓
Swap their values
 ↓
Valid BST
```

---

## LeetCode Information

**Problem Number:** 99  
**Problem Name:** Recover Binary Search Tree  
**Difficulty:** Medium  
**Topic:** Binary Tree, BST, Inorder Traversal

---

## File Structure

```text
99-recover-binary-search-tree/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](solution.py)

---

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
