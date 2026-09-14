```markdown
# 95. Unique Binary Search Trees II

**Difficulty:** Medium  
**Language:** Python

## Problem

Given an integer `n`, we have to generate all structurally unique Binary Search Trees (BSTs) containing exactly `n` nodes.

The values of the nodes must be:

```text
1 to n
```

A Binary Search Tree follows this rule:

```text
Left subtree values < Root value < Right subtree values
```

We need to return all possible structurally unique BSTs.

---

## Examples

### Example 1

**Input:**

```text
n = 3
```

**Output:**

```text
[
 [1,null,2,null,3],
 [1,null,3,2],
 [2,1,3],
 [3,1,null,null,2],
 [3,2,null,1]
]
```

There are **5** structurally unique BSTs for `n = 3`.

Some of them look like:

```text
    1
     \
      2
       \
        3
```

```text
    2
   / \
  1   3
```

```text
      3
     /
    2
   /
  1
```

---

### Example 2

**Input:**

```text
n = 1
```

**Output:**

```text
[[1]]
```

There is only one possible BST.

---

## Approach

I use **recursion and backtracking-style tree construction**.

For every range of values, I try every possible value as the root.

For example, for:

```text
1 to 3
```

we can choose:

```text
1
2
3
```

as the root.

If `2` is selected as the root:

```text
Left values: 1
Right values: 3
```

So we generate all possible left and right subtrees and combine them.

The same process is repeated recursively for smaller ranges.

---

## Algorithm

1. Create a recursive function `build(start, end)`.
2. If `start > end`, return `[None]` because an empty subtree is also a valid possibility.
3. Try every value from `start` to `end` as the root.
4. Recursively generate all possible left subtrees.
5. Recursively generate all possible right subtrees.
6. Combine every left subtree with every right subtree.
7. Create a new `TreeNode` for every combination.
8. Add each tree to the result list.
9. Return all generated trees.
10. Start the process with:

```text
build(1, n)
```

---

## Code

```python
class Solution:
    def generateTrees(self, n):
        def build(start, end):
            trees = []

            if start > end:
                return [None]

            for root_value in range(start, end + 1):
                left_trees = build(start, root_value - 1)
                right_trees = build(root_value + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_value)
                        root.left = left
                        root.right = right

                        trees.append(root)

            return trees

        return build(1, n)
```

---

## Dry Run

Let's take:

```text
n = 3
```

We call:

```text
build(1, 3)
```

### Root = 1

If `1` is the root:

```text
1
 \
  ?
```

Left subtree:

```text
None
```

Right subtree can be formed using:

```text
2, 3
```

Possible right subtrees:

```text
2
 \
  3
```

and

```text
  3
 /
2
```

So we get:

```text
1
 \
  2
   \
    3
```

and

```text
1
 \
  3
 /
2
```

---

### Root = 2

If `2` is the root:

```text
  2
 / \
?   ?
```

Left side contains:

```text
1
```

Right side contains:

```text
3
```

So:

```text
  2
 / \
1   3
```

is generated.

---

### Root = 3

If `3` is the root:

```text
    3
   /
  ?
```

The left side contains `1` and `2`.

Two possible left subtrees are:

```text
  1
   \
    2
```

and

```text
    2
   /
  1
```

So we get two more trees.

Therefore:

```text
Total = 2 + 1 + 2 = 5
```

---

## How Code Works

### 1. Handle Empty Subtree

```python
if start > end:
    return [None]
```

If there are no values available, we return `None`.

This is important because the parent node can have an empty left or right child.

---

### 2. Choose Root

```python
for root_value in range(start, end + 1):
```

Every value is tried as the root.

For example:

```text
1, 2, 3
```

can all become the root when `n = 3`.

---

### 3. Generate Left Subtrees

```python
left_trees = build(start, root_value - 1)
```

All values smaller than the root belong to the left subtree.

---

### 4. Generate Right Subtrees

```python
right_trees = build(root_value + 1, end)
```

All values greater than the root belong to the right subtree.

---

### 5. Combine Subtrees

```python
for left in left_trees:
    for right in right_trees:
```

Every possible left subtree is combined with every possible right subtree.

For each combination:

```python
root = TreeNode(root_value)
root.left = left
root.right = right
```

Then the complete tree is added to the result.

---

## Important Edge Cases

### 1. `n = 1`

Only one tree is possible:

```text
1
```

Output:

```text
[[1]]
```

### 2. Root at the Smallest Value

If `1` is selected as the root, there is no left subtree.

```text
1
 \
 ...
```

### 3. Root at the Largest Value

If `n` is selected as the root, there is no right subtree.

```text
    n
   /
  ...
```

### 4. Empty Subtree

An empty subtree is represented by:

```python
None
```

This allows trees with missing left or right children to be generated correctly.

---

## Number of Unique BSTs

The number of structurally unique BSTs follows the **Catalan numbers**.

For example:

```text
n = 1 → 1
n = 2 → 2
n = 3 → 5
n = 4 → 14
n = 5 → 42
n = 6 → 132
n = 7 → 429
n = 8 → 1430
```

Since the constraint is only:

```text
1 <= n <= 8
```

generating all trees is practical.

---

## Complexity Analysis

The number of trees generated is the `n`th Catalan number.

Let `C(n)` be the number of unique BSTs.

For `n = 8`:

```text
C(8) = 1430
```

**Time Complexity:** Approximately `O(C(n) × n)`

because we generate `C(n)` trees and each tree contains `n` nodes.

**Space Complexity:** `O(C(n) × n)`

because all generated trees need to be stored in the output.

---

## Key Concept

The main concepts used in this problem are:

- Recursion
- Binary Search Tree
- Divide and Conquer
- Backtracking-style generation
- Catalan Numbers

The important idea is:

```text
Choose Root
     ↓
Generate all Left Subtrees
     ↓
Generate all Right Subtrees
     ↓
Combine Left + Root + Right
```

---

## Constraints

- `1 <= n <= 8`
- Node values are unique.
- Node values range from `1` to `n`.
- All structurally unique BSTs must be returned.

---

## LeetCode Information

**Problem Number:** 95  
**Problem Name:** Unique Binary Search Trees II  
**Difficulty:** Medium  
**Topic:** Binary Tree, Binary Search Tree, Recursion, Backtracking

---

## File Structure

```text
95-unique-binary-search-trees-ii/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/95-unique-binary-search-trees-ii/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
