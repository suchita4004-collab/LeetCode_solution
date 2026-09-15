```markdown
# 98. Validate Binary Search Tree

**Difficulty:** Medium  
**Language:** Python

## Problem

Given the root of a binary tree, determine whether it is a valid **Binary Search Tree (BST)**.

A valid BST follows these rules:

- Every value in the left subtree must be **strictly smaller** than the current node.
- Every value in the right subtree must be **strictly greater** than the current node.
- The left and right subtrees must also be valid BSTs.

---

## Examples

### Example 1

**Input:**

```text
root = [2,1,3]
```

Tree:

```text
    2
   / \
  1   3
```

**Output:**

```text
true
```

The left value `1` is smaller than `2`, and the right value `3` is greater than `2`.

Therefore, it is a valid BST.

---

### Example 2

**Input:**

```text
root = [5,1,4,null,null,3,6]
```

Tree:

```text
      5
     / \
    1   4
       / \
      3   6
```

**Output:**

```text
false
```

The right subtree of `5` must contain values greater than `5`.

However, `4` is less than `5`.

Therefore, it is not a valid BST.

---

## Approach

I use **recursion with a valid range** for every node.

For each node, I keep two values:

```text
low
high
```

The current node's value must satisfy:

```text
low < node.val < high
```

For the left child:

```text
low < node.val < current node
```

For the right child:

```text
current node < node.val < high
```

This is important because checking only the direct children is not enough.

For example:

```text
      5
     / \
    1   7
       /
      4
```

The node `4` is smaller than `7`, so it looks correct when compared with its parent.

But `4` is in the right subtree of `5`, so it must be greater than `5`.

Therefore, the whole tree is invalid.

---

## Algorithm

1. Start with the root and an unrestricted range:

```text
(-infinity, +infinity)
```

2. For every node:
   - Check whether its value is inside the allowed range.
3. If it is outside the range, return `False`.
4. For the left subtree:
   - Keep the same lower limit.
   - Change the upper limit to the current node's value.
5. For the right subtree:
   - Change the lower limit to the current node's value.
   - Keep the same upper limit.
6. If all nodes satisfy their ranges, return `True`.

---

## Code

```python
class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))
```

---

## Dry Run

Consider:

```text
root = [2,1,3]
```

Tree:

```text
    2
   / \
  1   3
```

### Step 1: Check root `2`

Initial range:

```text
-infinity < 2 < infinity
```

Valid.

### Step 2: Check left node `1`

For the left subtree, the range becomes:

```text
-infinity < 1 < 2
```

Valid.

### Step 3: Check right node `3`

For the right subtree, the range becomes:

```text
2 < 3 < infinity
```

Valid.

All nodes are valid.

Therefore:

```text
Output = true
```

---

## Dry Run for Invalid Tree

Consider:

```text
root = [5,1,4,null,null,3,6]
```

Tree:

```text
      5
     / \
    1   4
       / \
      3   6
```

For root `5`:

```text
-infinity < 5 < infinity
```

Valid.

For node `4` in the right subtree:

```text
5 < 4 < infinity
```

This is false because:

```text
4 < 5
```

Therefore, the function returns:

```text
false
```

---

## How Code Works

### 1. Recursive Function

```python
def validate(node, low, high):
```

This function checks whether a node is valid within a specific range.

---

### 2. Empty Node

```python
if node is None:
    return True
```

An empty subtree is considered valid.

---

### 3. Check Current Node

```python
if node.val <= low or node.val >= high:
    return False
```

The value must be **strictly** between `low` and `high`.

Strict comparison is important because duplicate values are not allowed in a valid BST.

---

### 4. Check Left Subtree

```python
validate(node.left, low, node.val)
```

Every value in the left subtree must be smaller than the current node.

---

### 5. Check Right Subtree

```python
validate(node.right, node.val, high)
```

Every value in the right subtree must be greater than the current node.

---

## Important BST Rule

The important point is that the restriction applies to the **entire subtree**, not just the direct child.

For example:

```text
        10
       /  \
      5    15
          /
         6
```

`6 < 15`, so it is smaller than its parent.

But `6` is in the right subtree of `10`.

Therefore:

```text
6 must be > 10
```

It is not, so the tree is invalid.

The range method catches this automatically.

---

## Duplicate Values

A valid BST requires values to be **strictly** less or greater.

This tree is invalid:

```text
    2
   / \
  2   3
```

because the left value is equal to the root.

Similarly:

```text
    2
   / \
  1   2
```

is invalid because the right value is equal to the root.

---

## Complexity Analysis

Let `n` be the number of nodes.

**Time Complexity:** `O(n)`

Every node is visited once.

**Space Complexity:** `O(h)`

where `h` is the height of the tree because of the recursion stack.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```

---

## Key Concept

The main concept used in this problem is **Range Validation**.

Each node gets an allowed range:

```text
             (-∞, +∞)
                  |
                 10
              /      \
        (-∞,10)    (10,+∞)
```

The range becomes smaller as we move down the tree.

This ensures that every node follows the BST rule with respect to all of its ancestors.

---

## Constraints

- The number of nodes is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`.
- Values must be strictly less or greater.
- Duplicate values are not allowed.

---

## LeetCode Information

**Problem Number:** 98  
**Problem Name:** Validate Binary Search Tree  
**Difficulty:** Medium  
**Topic:** Binary Tree, Binary Search Tree, Recursion, DFS

---

## File Structure

```text
98-validate-binary-search-tree/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/98-validate-binary-search-tree/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
