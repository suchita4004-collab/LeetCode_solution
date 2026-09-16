```markdown
# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Language:** Python

---

## Problem

Given the root of a binary tree, return its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The longest path is:

```text
3 → 20 → 15
```

It contains 3 nodes.

Therefore, the maximum depth is:

```text
3
```

---

## Examples

### Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
3
```

**Explanation:**

The longest path from the root to a leaf contains 3 nodes.

```text
3 → 20 → 15
```

or

```text
3 → 20 → 7
```

Therefore, the maximum depth is `3`.

---

### Example 2

**Input:**

```text
root = [1,null,2]
```

**Output:**

```text
2
```

**Explanation:**

The longest path is:

```text
1 → 2
```

Therefore, the maximum depth is `2`.

---

## Approach

We use **recursion**.

For every node:

1. Find the maximum depth of its left subtree.
2. Find the maximum depth of its right subtree.
3. Take the larger of the two.
4. Add `1` for the current node.

The formula is:

```text
Maximum Depth = 1 + max(left depth, right depth)
```

For an empty tree, the depth is `0`.

---

## Algorithm

```text
1. If root is None:
       return 0

2. Find the maximum depth of the left subtree.

3. Find the maximum depth of the right subtree.

4. Take the maximum of the left and right depths.

5. Add 1 for the current root node.

6. Return the result.
```

---

## Dry Run

Consider:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Step 1

Start at root:

```text
3
```

Check its left and right subtrees.

---

### Step 2

Left subtree:

```text
9
```

Node `9` has no children.

Therefore:

```text
Depth of 9 = 1
```

---

### Step 3

Right subtree:

```text
       20
      /  \
     15   7
```

Both `15` and `7` are leaf nodes.

So:

```text
Depth of 15 = 1
Depth of 7  = 1
```

For node `20`:

```text
1 + max(1, 1) = 2
```

Therefore:

```text
Depth of 20 = 2
```

---

### Step 4

Now calculate the depth of root `3`:

```text
1 + max(1, 2)
```

```text
1 + 2 = 3
```

Final answer:

```text
3
```

---

## How the Code Works

### 1. Check for an empty tree

```python
if root is None:
    return 0
```

If there is no node, the depth is `0`.

---

### 2. Find left depth

```python
left_depth = self.maxDepth(root.left)
```

The function recursively finds the maximum depth of the left subtree.

---

### 3. Find right depth

```python
right_depth = self.maxDepth(root.right)
```

The same process is performed for the right subtree.

---

### 4. Take the larger depth

```python
max(left_depth, right_depth)
```

The maximum depth must come from either the left or right subtree.

---

### 5. Add the current node

```python
return 1 + max(left_depth, right_depth)
```

The `1` represents the current node.

---

## Important Edge Cases

### 1. Empty tree

```text
root = []
```

Output:

```text
0
```

---

### 2. Single node

```text
    1
```

Output:

```text
1
```

There is only one node in the longest path.

---

### 3. Only left child

```text
    1
   /
  2
 /
3
```

Output:

```text
3
```

---

### 4. Only right child

```text
1
 \
  2
   \
    3
```

Output:

```text
3
```

---

## Recursive Working

The recursive calls work from the bottom of the tree upward.

For:

```text
        1
       / \
      2   3
```

The calculation is:

```text
Depth(2) = 1
Depth(3) = 1

Depth(1) = 1 + max(1, 1)
         = 2
```

Therefore:

```text
Maximum Depth = 2
```

---

## Complexity Analysis

Let `n` be the number of nodes in the tree.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once.

### Space Complexity

```text
O(h)
```

The recursive call stack depends on the height `h` of the tree.

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

The main idea is:

```text
              Root
                |
        ┌───────┴───────┐
        ↓               ↓
   Left Depth      Right Depth
        ↓               ↓
        └───────┬───────┘
                ↓
        Take maximum
                ↓
          Add 1 for root
                ↓
        Maximum Depth
```

In simple words:

> Find the deeper side of the tree and add one for the current node.

---

## Constraints

- Number of nodes is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`.

---

## LeetCode Information

**Problem Number:** 104  
**Problem Name:** Maximum Depth of Binary Tree  
**Difficulty:** Easy  
**Topics:** Binary Tree, Depth-First Search, Recursion

---

## File Structure

```text
104-maximum-depth-of-binary-tree/
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
``````markdown
# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Language:** Python

---

## Problem

Given the root of a binary tree, return its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The longest path is:

```text
3 → 20 → 15
```

It contains 3 nodes.

Therefore, the maximum depth is:

```text
3
```

---

## Examples

### Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
3
```

**Explanation:**

The longest path from the root to a leaf contains 3 nodes.

```text
3 → 20 → 15
```

or

```text
3 → 20 → 7
```

Therefore, the maximum depth is `3`.

---

### Example 2

**Input:**

```text
root = [1,null,2]
```

**Output:**

```text
2
```

**Explanation:**

The longest path is:

```text
1 → 2
```

Therefore, the maximum depth is `2`.

---

## Approach

We use **recursion**.

For every node:

1. Find the maximum depth of its left subtree.
2. Find the maximum depth of its right subtree.
3. Take the larger of the two.
4. Add `1` for the current node.

The formula is:

```text
Maximum Depth = 1 + max(left depth, right depth)
```

For an empty tree, the depth is `0`.

---

## Algorithm

```text
1. If root is None:
       return 0

2. Find the maximum depth of the left subtree.

3. Find the maximum depth of the right subtree.

4. Take the maximum of the left and right depths.

5. Add 1 for the current root node.

6. Return the result.
```

---

## Dry Run

Consider:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Step 1

Start at root:

```text
3
```

Check its left and right subtrees.

---

### Step 2

Left subtree:

```text
9
```

Node `9` has no children.

Therefore:

```text
Depth of 9 = 1
```

---

### Step 3

Right subtree:

```text
       20
      /  \
     15   7
```

Both `15` and `7` are leaf nodes.

So:

```text
Depth of 15 = 1
Depth of 7  = 1
```

For node `20`:

```text
1 + max(1, 1) = 2
```

Therefore:

```text
Depth of 20 = 2
```

---

### Step 4

Now calculate the depth of root `3`:

```text
1 + max(1, 2)
```

```text
1 + 2 = 3
```

Final answer:

```text
3
```

---

## How the Code Works

### 1. Check for an empty tree

```python
if root is None:
    return 0
```

If there is no node, the depth is `0`.

---

### 2. Find left depth

```python
left_depth = self.maxDepth(root.left)
```

The function recursively finds the maximum depth of the left subtree.

---

### 3. Find right depth

```python
right_depth = self.maxDepth(root.right)
```

The same process is performed for the right subtree.

---

### 4. Take the larger depth

```python
max(left_depth, right_depth)
```

The maximum depth must come from either the left or right subtree.

---

### 5. Add the current node

```python
return 1 + max(left_depth, right_depth)
```

The `1` represents the current node.

---

## Important Edge Cases

### 1. Empty tree

```text
root = []
```

Output:

```text
0
```

---

### 2. Single node

```text
    1
```

Output:

```text
1
```

There is only one node in the longest path.

---

### 3. Only left child

```text
    1
   /
  2
 /
3
```

Output:

```text
3
```

---

### 4. Only right child

```text
1
 \
  2
   \
    3
```

Output:

```text
3
```

---

## Recursive Working

The recursive calls work from the bottom of the tree upward.

For:

```text
        1
       / \
      2   3
```

The calculation is:

```text
Depth(2) = 1
Depth(3) = 1

Depth(1) = 1 + max(1, 1)
         = 2
```

Therefore:

```text
Maximum Depth = 2
```

---

## Complexity Analysis

Let `n` be the number of nodes in the tree.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once.

### Space Complexity

```text
O(h)
```

The recursive call stack depends on the height `h` of the tree.

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

The main idea is:

```text
              Root
                |
        ┌───────┴───────┐
        ↓               ↓
   Left Depth      Right Depth
        ↓               ↓
        └───────┬───────┘
                ↓
        Take maximum
                ↓
          Add 1 for root
                ↓
        Maximum Depth
```

In simple words:

> Find the deeper side of the tree and add one for the current node.

---

## Constraints

- Number of nodes is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`.

---

## LeetCode Information

**Problem Number:** 104  
**Problem Name:** Maximum Depth of Binary Tree  
**Difficulty:** Easy  
**Topics:** Binary Tree, Depth-First Search, Recursion

---

## File Structure

```text
104-maximum-depth-of-binary-tree/
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
