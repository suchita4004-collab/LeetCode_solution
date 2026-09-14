```markdown
# 94. Binary Tree Inorder Traversal

**Difficulty:** Easy  
**Language:** Python

## Problem

Given the root of a binary tree, return the values of its nodes in **inorder traversal**.

In inorder traversal, we visit the nodes in this order:

```text
Left → Root → Right
```

---

## Examples

### Example 1

**Input:**
```text
root = [1,null,2,3]
```

Tree:

```text
    1
     \
      2
     /
    3
```

**Inorder Traversal:**

```text
Left → Root → Right
```

```text
3 → 2
```

So the output is:

```text
[1,3,2]
```

### Example 2

**Input:**
```text
root = [1,2,3,4,5,null,8,null,null,6,7,9]
```

**Output:**
```text
[4,2,6,5,7,1,3,9,8]
```

### Example 3

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

### Example 4

**Input:**
```text
root = [1]
```

**Output:**
```text
[1]
```

---

## Approach

I use **recursion** to perform the inorder traversal.

For every node, we follow three steps:

1. Traverse the left subtree.
2. Add the current node's value to the result.
3. Traverse the right subtree.

This gives the required:

```text
Left → Root → Right
```

order.

---

## Algorithm

1. Create an empty list called `result`.
2. Create a recursive function `inorder(node)`.
3. If the current node is `None`, return.
4. Recursively visit the left child.
5. Add the current node's value to `result`.
6. Recursively visit the right child.
7. Start the traversal from `root`.
8. Return `result`.

---

## Code

```python
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result
```

---

## Dry Run

Consider:

```text
root = [1,null,2,3]
```

Tree:

```text
    1
     \
      2
     /
    3
```

Start at node `1`.

### Step 1
There is no left child of `1`.

### Step 2
Add `1`.

```text
result = [1]
```

### Step 3
Move to the right child `2`.

Node `2` has a left child `3`.

Visit `3` first:

```text
result = [1,3]
```

Then visit `2`:

```text
result = [1,3,2]
```

Final output:

```text
[1,3,2]
```

---

## How Code Works

### 1. Create Result List

```python
result = []
```

This list stores the values in inorder order.

### 2. Check for Empty Node

```python
if node is None:
    return
```

If there is no node, there is nothing to visit.

### 3. Visit Left Subtree

```python
inorder(node.left)
```

We first visit everything on the left side.

### 4. Visit Current Node

```python
result.append(node.val)
```

After the left subtree is completed, we add the current node.

### 5. Visit Right Subtree

```python
inorder(node.right)
```

Finally, we visit the right subtree.

So the complete order is:

```text
       Node
      /    \
     /      \
  Left     Right

     ↓
Left → Root → Right
```

---

## Important Edge Cases

### 1. Empty Tree

```text
Input: []
Output: []
```

The root is `None`, so the function immediately returns.

### 2. Single Node

```text
Input: [1]
Output: [1]
```

There is no left or right subtree.

### 3. Only Left Children

```text
      3
     /
    2
   /
  1
```

Inorder traversal:

```text
[1,2,3]
```

### 4. Only Right Children

```text
1
 \
  2
   \
    3
```

Inorder traversal:

```text
[1,2,3]
```

---

## Complexity Analysis

Let `n` be the number of nodes in the binary tree.

**Time Complexity:** `O(n)`

Every node is visited exactly once.

**Space Complexity:** `O(n)`

The recursion stack can contain up to `n` nodes in the worst case when the tree is completely skewed.

The `result` list also contains `n` values.

---

## Key Concept

The main concept used in this problem is **Tree Traversal**.

There are three common depth-first traversals:

```text
Preorder:
Root → Left → Right

Inorder:
Left → Root → Right

Postorder:
Left → Right → Root
```

For this problem, we specifically need:

```text
Left → Root → Right
```

---

## Constraints

- The number of nodes is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`.

---

## LeetCode Information

**Problem Number:** 94  
**Problem Name:** Binary Tree Inorder Traversal  
**Difficulty:** Easy  
**Topic:** Binary Tree, DFS, Recursion, Tree Traversal

---

## File Structure

```text
94-binary-tree-inorder-traversal/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/94-binary-tree-inorder-traversal/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
