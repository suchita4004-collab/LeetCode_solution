```markdown
# 105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium  
**Language:** Python

---

## Problem

Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

The arrays represent the traversals of the same binary tree.

### Preorder Traversal

Preorder visits nodes in this order:

```text
Root → Left → Right
```

### Inorder Traversal

Inorder visits nodes in this order:

```text
Left → Root → Right
```

We use these two traversals to reconstruct the original binary tree.

---

## Examples

### Example 1

**Input:**

```text
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

**Output:**

```text
[3,9,20,null,null,15,7]
```

The constructed tree is:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Preorder:

```text
3 → 9 → 20 → 15 → 7
```

Inorder:

```text
9 → 3 → 15 → 20 → 7
```

---

### Example 2

**Input:**

```text
preorder = [-1]
inorder = [-1]
```

**Output:**

```text
[-1]
```

The tree contains only one node:

```text
    -1
```

---

## Approach

The important observation is:

### Preorder

```text
Root → Left → Right
```

So, the **first element of preorder is always the root** of the current subtree.

### Inorder

```text
Left → Root → Right
```

Once we find the root in inorder:

```text
Left side of root  → Left subtree
Right side of root → Right subtree
```

Therefore, we can recursively build the tree.

---

## Example

Given:

```text
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

First element of preorder:

```text
3
```

So `3` is the root.

Find `3` in inorder:

```text
[9, 3, 15, 20, 7]
    ↑
   root
```

Therefore:

```text
Left subtree  = [9]
Right subtree = [15,20,7]
```

The tree starts as:

```text
        3
       / \
      9   ?
```

Now repeat the same process for the right subtree.

---

## Algorithm

```text
1. Create a dictionary containing each inorder value
   and its index.

2. Start preorder_index at 0.

3. Take preorder[preorder_index] as the root.

4. Find the root's position in inorder.

5. Everything before the root belongs to the left subtree.

6. Everything after the root belongs to the right subtree.

7. Recursively build the left subtree.

8. Recursively build the right subtree.

9. Return the root.
```

---

## Dry Run

Consider:

```text
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

### Step 1: Root

First preorder element:

```text
3
```

So:

```text
        3
```

Find `3` in inorder:

```text
[9, 3, 15, 20, 7]
    ↑
```

Left:

```text
[9]
```

Right:

```text
[15,20,7]
```

---

### Step 2: Build left subtree

Next preorder element:

```text
9
```

Inorder range contains only:

```text
[9]
```

So `9` becomes the left child:

```text
        3
       /
      9
```

---

### Step 3: Build right subtree

Next preorder element:

```text
20
```

Inorder:

```text
[15,20,7]
```

`20` is the root of this subtree.

Left:

```text
[15]
```

Right:

```text
[7]
```

So:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

### Final Tree

```text
        3
       / \
      9   20
         /  \
        15   7
```

Output:

```text
[3,9,20,null,null,15,7]
```

---

## How the Code Works

### 1. Store inorder positions

```python
inorder_index = {
    value: index for index, value in enumerate(inorder)
}
```

For:

```text
inorder = [9,3,15,20,7]
```

The dictionary becomes:

```text
9  → 0
3  → 1
15 → 2
20 → 3
7  → 4
```

This allows us to find the root position in `O(1)` time.

---

### 2. Track preorder

```python
preorder_index = 0
```

This keeps track of which preorder element should be used next.

---

### 3. Create the root

```python
root_value = preorder[preorder_index]
preorder_index += 1

root = TreeNode(root_value)
```

Since preorder starts with the root, the current preorder value becomes the root.

---

### 4. Find root in inorder

```python
mid = inorder_index[root_value]
```

This divides the inorder array into:

```text
Left subtree | Root | Right subtree
```

---

### 5. Build left subtree

```python
root.left = build(left, mid - 1)
```

All values before the root in inorder belong to the left subtree.

---

### 6. Build right subtree

```python
root.right = build(mid + 1, right)
```

All values after the root belong to the right subtree.

---

## Important Edge Cases

### 1. Single node

```text
preorder = [1]
inorder = [1]
```

Output:

```text
[1]
```

---

### 2. Completely left-skewed tree

```text
preorder = [3,2,1]
inorder = [1,2,3]
```

Tree:

```text
        3
       /
      2
     /
    1
```

---

### 3. Completely right-skewed tree

```text
preorder = [1,2,3]
inorder = [1,2,3]
```

Tree:

```text
1
 \
  2
   \
    3
```

---

### 4. Balanced tree

```text
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

## Why Does This Work?

Preorder tells us:

```text
Who is the root?
```

Inorder tells us:

```text
Which nodes belong to the left and right subtrees?
```

Together:

```text
Preorder + Inorder
        ↓
Find Root
        ↓
Split Inorder
   ↙          ↘
Left          Right
Subtree       Subtree
   ↓             ↓
Recursively build both
        ↓
Complete Tree
```

Because all values are unique, every root has exactly one position in the inorder array.

---

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

Each node is processed once.

The dictionary allows us to find the position of a value in inorder in `O(1)` average time.

### Space Complexity

```text
O(n)
```

The inorder dictionary stores `n` values.

The recursion stack requires `O(h)` space, where `h` is the height of the tree.

Therefore, the total auxiliary space is:

```text
O(n)
```

in the worst case.

---

## Key Concept

The most important idea is:

```text
Preorder:
Root → Left → Right

Inorder:
Left → Root → Right
```

Therefore:

```text
First element of Preorder
          ↓
        ROOT
          ↓
Find ROOT in Inorder
       ↙     ↘
    Left     Right
   subtree  subtree
       ↓      ↓
     Recursively build
```

---

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` contain unique values.
- Every value in `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be a valid preorder traversal.
- `inorder` is guaranteed to be a valid inorder traversal.

---

## LeetCode Information

**Problem Number:** 105  
**Problem Name:** Construct Binary Tree from Preorder and Inorder Traversal  
**Difficulty:** Medium  
**Topics:** Binary Tree, Array, Hash Table, Divide and Conquer, Recursion

---

## File Structure

```text
105-construct-binary-tree-from-preorder-and-inorder-traversal/
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
