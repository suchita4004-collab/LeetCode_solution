# 106. Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium  
**Language:** Python

## Problem

Given two integer arrays `inorder` and `postorder`, where:

- `inorder` is the inorder traversal of a binary tree.
- `postorder` is the postorder traversal of the same binary tree.

Construct and return the original binary tree.

### Traversal Order

**Inorder:**

```text
Left → Root → Right
```

**Postorder:**

```text
Left → Right → Root
```

The important observation is that the **last element of postorder is always the root** of the current tree.

## Examples

### Example 1

**Input:**
```text
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

**Output:**
```text
[3,9,20,null,null,15,7]
```

The tree is:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Example 2

**Input:**
```text
inorder = [-1]
postorder = [-1]
```

**Output:**
```text
[-1]
```

## Approach

We can construct the tree using the following steps:

1. Store the index of every value in the `inorder` array using a dictionary.
2. Start from the **last element of `postorder`**, because it is the root.
3. Find the root's position in `inorder`.
4. Elements to the left of the root belong to the left subtree.
5. Elements to the right of the root belong to the right subtree.
6. Since we are reading `postorder` from right to left, we must construct the **right subtree first**.
7. Continue recursively until the subtree becomes empty.

## Algorithm

```text
Create a dictionary containing the index of each value in inorder.

Set postorder_index to the last index of postorder.

Build the tree recursively:

    If the current inorder range is empty:
        return None

    Take postorder[postorder_index] as the root.
    Decrease postorder_index.

    Find the root position in inorder.

    Build the right subtree first.
    Build the left subtree.

    Return the root.
```

## Dry Run

For:

```text
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
```

### Step 1

Last element of postorder is `3`.

So:

```text
Root = 3
```

In inorder:

```text
[9, 3, 15, 20, 7]
    ↑
   root
```

Left subtree:

```text
[9]
```

Right subtree:

```text
[15,20,7]
```

### Step 2

Move backwards in postorder.

Next value is `20`.

So `20` becomes the right child of `3`.

```text
    3
     \
      20
```

### Step 3

Next value is `7`.

It belongs to the right subtree of `20`.

```text
    3
     \
      20
        \
         7
```

### Step 4

Next value is `15`.

It becomes the left child of `20`.

```text
      3
       \
        20
       /  \
      15   7
```

Finally, `9` becomes the left child of `3`.

```text
        3
       / \
      9   20
         /  \
        15   7
```

Therefore:

```text
Output = [3,9,20,null,null,15,7]
```

## How the Code Works

The dictionary gives the position of each value in `inorder` in **O(1)** average time.

For example:

```python
inorder_index = {
    9: 0,
    3: 1,
    15: 2,
    20: 3,
    7: 4
}
```

We start from the end of `postorder`:

```python
postorder_index = len(postorder) - 1
```

For the first call:

```text
postorder[4] = 3
```

So `3` is the root.

After using `3`, we move backwards:

```python
postorder_index -= 1
```

Because postorder is:

```text
Left → Right → Root
```

and we are processing it backwards:

```text
Root → Right → Left
```

we build the **right subtree before the left subtree**.

## Important Edge Cases

### 1. Single node

```text
inorder = [-1]
postorder = [-1]
```

The tree contains only one node.

### 2. Completely left-skewed tree

Each node has only a left child.

### 3. Completely right-skewed tree

Each node has only a right child.

### 4. Large input

The solution uses a dictionary to find root positions quickly, making it efficient for up to 3000 nodes.

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

Each node is processed once, and its position in `inorder` is found in O(1) average time.

### Space Complexity

```text
O(n)
```

The dictionary stores `n` values, and the recursion can also use up to `O(n)` stack space in a skewed tree.

## Key Concept

The main idea is:

```text
Inorder:   Left → Root → Right
Postorder: Left → Right → Root
```

Therefore:

```text
Last element of Postorder = Root
```

After finding the root in inorder:

```text
        Root
       /    \
    Left    Right
```

When processing postorder backwards:

```text
Root → Right → Left
```

So the **right subtree must be constructed first**.

## Constraints

- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- All values are unique.
- Every value in `postorder` also appears in `inorder`.
- The given arrays are valid traversals of the same binary tree.

## LeetCode Information

- **Problem:** Construct Binary Tree from Inorder and Postorder Traversal
- **Problem Number:** 106
- **Difficulty:** Medium
- **Language:** Python

## File Structure

```text
106-construct-binary-tree-from-inorder-and-postorder-traversal/
│
├── README.md
└── solution.py
```

## Solution

See [`solution.py`](solution.py) for the complete Python solution.

## Repository

**GitHub Repository:** `LeetCode_solution`
