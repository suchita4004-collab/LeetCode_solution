# 110. Balanced Binary Tree

**Difficulty:** Easy  
**Language:** Python

## Problem

Given the root of a binary tree, determine whether the tree is **height-balanced**.

A binary tree is height-balanced if, for every node, the difference between the heights of its left and right subtrees is **at most 1**.

In other words:

```text
| height(left) - height(right) | <= 1
```

## Examples

### Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The left and right subtree heights differ by at most 1.

**Output:**

```text
true
```

### Example 2

**Input:**

```text
root = [1,2,2,3,3,null,null,4,4]
```

Tree:

```text
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4
```

The left subtree is much deeper than the right subtree.

**Output:**

```text
false
```

### Example 3

**Input:**

```text
root = []
```

An empty tree is considered height-balanced.

**Output:**

```text
true
```

## Approach

We need to check the height of every subtree.

A simple approach would be:

1. Calculate the height of the left subtree.
2. Calculate the height of the right subtree.
3. Check their difference.
4. Repeat this for every node.

However, calculating heights repeatedly can make the solution slow.

Instead, we use a **bottom-up recursion**.

For every node:

- Get the height of the left subtree.
- Get the height of the right subtree.
- If either subtree is already unbalanced, return `-1`.
- If the height difference is greater than `1`, return `-1`.
- Otherwise, return the height of the current subtree.

Here, `-1` is used as a special value to indicate that the subtree is not balanced.

## Algorithm

```text
1. If the node is None, return height 0.

2. Recursively find the height of the left subtree.

3. If the left subtree is unbalanced, return -1.

4. Recursively find the height of the right subtree.

5. If the right subtree is unbalanced, return -1.

6. If the difference between left and right heights is
   greater than 1, return -1.

7. Otherwise, return:
      1 + maximum(left height, right height)

8. The tree is balanced if the final result is not -1.
```

## Dry Run

For:

```text
root = [3,9,20,null,null,15,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Node 9

```text
Left height  = 0
Right height = 0

Difference = 0
```

Height of node `9`:

```text
1
```

### Node 20

Both children have height `1`:

```text
Left height  = 1
Right height = 1

Difference = 0
```

Height of node `20`:

```text
2
```

### Node 3

```text
Left height  = 1
Right height = 2

Difference = 1
```

Since the difference is not greater than 1, the tree is balanced.

Therefore:

```text
Output = true
```

## How the Code Works

The helper function returns the height of a subtree.

```python
def height(node):
    if node is None:
        return 0
```

We calculate the left subtree height:

```python
left = height(node.left)
```

If it returns `-1`, the left subtree is unbalanced:

```python
if left == -1:
    return -1
```

Then we calculate the right subtree:

```python
right = height(node.right)

if right == -1:
    return -1
```

Now we check the height difference:

```python
if abs(left - right) > 1:
    return -1
```

If everything is balanced, return the height:

```python
return 1 + max(left, right)
```

Finally:

```python
return height(root) != -1
```

If the final value is not `-1`, the entire tree is balanced.

## Important Edge Cases

### 1. Empty tree

```text
root = []
```

An empty tree is balanced.

```text
true
```

### 2. Single node

```text
root = [1]
```

Both subtree heights are `0`, so it is balanced.

```text
true
```

### 3. Completely skewed tree

For example:

```text
    1
     \
      2
       \
        3
         \
          4
```

The height difference becomes greater than 1, so the tree is not balanced.

```text
false
```

## Complexity Analysis

Let `n` be the number of nodes in the tree.

### Time Complexity

```text
O(n)
```

Each node is visited only once.

### Space Complexity

```text
O(h)
```

where `h` is the height of the tree.

The space is used by the recursion stack.

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```

## Key Concept

A tree is height-balanced when:

```text
|height(left) - height(right)| <= 1
```

The important optimization is to check the balance **while calculating height**, instead of calculating the height separately for every node.

```text
             Node
            /    \
       Left       Right
      Height      Height
         \          /
          \        /
       Difference <= 1
```

Using `-1` as a special value allows an unbalanced subtree to immediately inform its parent.

## Constraints

- Number of nodes is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`.

## LeetCode Information

- **Problem:** Balanced Binary Tree
- **Problem Number:** 110
- **Difficulty:** Easy
- **Language:** Python

## File Structure

```text
110-balanced-binary-tree/
│
├── README.md
└── solution.py
```

## Solution

See [`solution.py`](solution.py) for the complete Python solution.

## Repository

**GitHub Repository:** `LeetCode_solution`
